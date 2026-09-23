// Read-only checks, invoked from a GM macro after importing into the test world.
export async function validateImportedWorld() {
  if (!game.user.isGM) throw new Error('GM session required');
  if (game.world.title !== 'DnD5e-6.0.3-Testing') throw new Error('Wrong test world');
  const root='/modules/translate-dnd5e-tomb-annihilation-es';
  const response=await fetch(`${root}/dev-tools/export/data/world-validation-expectations.json`,{cache:'no-store'});
  if (!response.ok) throw new Error('Run prepare_world_validation.py first');
  const expected=await response.json();
  const report={date:new Date().toISOString(),world:game.world.title,foundry:game.version,system:game.system.version,
    language:game.settings.get('core','language'),counts:{},checked:0,fieldErrors:[],images:[],references:[]};
  const cache=new Map();
  for (const [kind,count] of Object.entries(expected.counts)) report.counts[kind]={expected:count,actual:game.collections.get(kind).size};
  for (const check of expected.checks) {
    const key=`${check.kind}.${check.id}`;
    if (!cache.has(key)) cache.set(key,game.collections.get(check.kind)?.get(check.id)?.toObject());
    let value=cache.get(key);
    for (const part of check.path) value=Array.isArray(value) ? value.find(v=>v?._id===part) : value?.[part];
    report.checked++;
    if ((typeof value==='string'?value.trim():value)!==check.expected.trim()) report.fieldErrors.push({key,path:check.path,expected:check.expected,actual:value});
    if (check.path.at(-1)==='src') {
      const image=new Image(); image.src=value;
      try {await image.decode();report.images.push({src:value,width:image.naturalWidth,height:image.naturalHeight});}
      catch {report.images.push({src:value,error:'Image failed to decode'});}
    }
  }
  const references=[...new Set(expected.references.filter(r=>r.type==='uuid').map(r=>r.reference))];
  for (const reference of references) {
    try {const doc=await fromUuid(reference);report.references.push({reference,resolved:!!doc,name:doc?.name});}
    catch(error){report.references.push({reference,resolved:false,error:error.message});}
  }
  console.log('TOA_IMPORTED_WORLD_RESULT '+JSON.stringify({...report,fieldErrorCount:report.fieldErrors.length,fieldErrors:report.fieldErrors.slice(0,12)}));
  ui.notifications.info(`ToA: ${report.checked} campos; ${report.fieldErrors.length} diferencias; ${report.images.length} imágenes comprobadas.`);
  return report;
}

// Explicit repair for this disposable test world only. Never run automatically.
export async function restoreReviewedTokenNames() {
  const report=await validateImportedWorld();
  if (game.settings.get('babele','syncImportedAdventureTokenNames') !== false) {
    throw new Error('Disable Babele token name synchronization before repairing');
  }
  const updates=new Map();
  for (const error of report.fieldErrors) {
    if (!error.key.startsWith('Scene.') || error.path.length!==3 || error.path[0]!=='tokens' || error.path[2]!=='name') {
      throw new Error('Unexpected difference: refusing partial repair');
    }
    const scene=game.scenes.get(error.key.split('.')[1]);
    const token=scene.tokens.get(error.path[1]);
    if (token.name!==error.actual || game.actors.get(token.actorId)?.prototypeToken.name!==error.actual) {
      throw new Error('Token differs from Babele synchronization result: refusing repair');
    }
    if (!updates.has(scene.id)) updates.set(scene.id,[]);
    updates.get(scene.id).push({_id:token.id,name:error.expected});
  }
  console.log('TOA_TOKEN_REPAIR_BACKUP '+JSON.stringify(report.fieldErrors));
  for (const [id,changes] of updates) await game.scenes.get(id).updateEmbeddedDocuments('Token',changes);
  return validateImportedWorld();
}
