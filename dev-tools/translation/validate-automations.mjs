// Run explicitly from the GM validation macro in the disposable testing world.
export async function validateAutomations() {
  if (!game.user.isGM || !game.world.title.startsWith('DnD5e-6.0.3-Testing')) throw Error('Test GM world required');
  const report = {date: new Date().toISOString(), world: game.world.title, checks: [], errors: []};
  async function check(name, run) {
    try {report.checks.push({name, result: await run()});}
    catch (error) {report.errors.push({name, error: String(error)});}
  }
  const root = '/modules/translate-dnd5e-tomb-annihilation-es';
  const compatibility = await import(`${root}/scripts/mirrored-scenes.mjs?validation=2`);
  await check('Mirrored scenes: stable IDs and installed replacement', async () => {
    if (!compatibility.installMirroredSceneCompatibility()) throw Error('Replacement not installed');
    const adventure = await fromUuid('Compendium.dnd-tomb-annihilation.adventures.Adventure.OQ0bB1QgjuxagwGI');
    return compatibility.mirroredScenePairs(adventure, game.scenes).map(p => ({id:p.scene.id,name:p.scene.name}));
  });
  const macros = game.modules.get('dnd-tomb-annihilation').macros;
  async function toggle(name, uuid, field, action) {
    await check(name, async () => {
      const doc = await fromUuid(uuid);
      if (!doc) throw Error(`Missing ${uuid}`);
      const before = doc[field];
      try {
        await action();
        const after = doc[field];
        if (after === before) throw Error('State did not change');
        await action();
        if (doc[field] !== before) throw Error('Second activation did not restore state');
        return {uuid,before,after,restored:doc[field]};
      } finally {
        if (doc[field] !== before) await doc.update({[field]:before});
      }
    });
  }
  await toggle('Concealed spike trap','Scene.toaWyrmheartMine.Tile.WacPEIdxQILr9mUU','hidden',()=>macros.ch2.toggleConcealedSpikeTrap());
  await toggle('Black drape','Scene.toaLevel3Vaultof.Tile.JKPveY5Ueo1Ieonk','hidden',()=>macros.gen.toggleTiles(['Scene.toaLevel3Vaultof.Tile.JKPveY5Ueo1Ieonk']));
  await toggle('Hrakhamar walkway','Scene.toaHrakhamar0000.Tile.jCpK7DZuKG6KzmRp','hidden',()=>macros.gen.toggleTiles(['Scene.toaHrakhamar0000.Tile.jCpK7DZuKG6KzmRp']));
  await toggle('Gas light','Scene.toaCh3FaneoftheN.AmbientLight.wuNnSNBPy9Szp315','hidden',()=>macros.gen.toggleLights(['Scene.toaCh3FaneoftheN.AmbientLight.wuNnSNBPy9Szp315']));
  await toggle('Ooze obelisk teleporter switch','Scene.toaCh5Level6Crad.Region.AFDOMqn09MompJsE.RegionBehavior.G5lf7XNZswTCj8ia','disabled',()=>macros.ch5.ar81.toggleOozeObelisk());
  await check('Atropal attack and damage', async () => {
    const actor = await game.packs.get('dnd-tomb-annihilation.actors').getDocument('dbM4sT1yZLbnZR2a');
    const item = actor.items.get('MSvn8c3HoaylytpC');
    const activity = item.system.activities.find(a=>a.type==='attack');
    const attack = await activity.rollAttack({}, {configure:false}, {create:false});
    const damage = await activity.rollDamage({}, {configure:false}, {create:false});
    if (!attack?.length || !damage?.length) throw Error('Missing rolls');
    return {item:item.name,attack:attack.map(r=>({formula:r.formula,total:r.total})),damage:damage.map(r=>({formula:r.formula,total:r.total}))};
  });
  await check('Valindra spell damage', async () => {
    const actor = game.actors.get('toaValindraShado');
    const item = actor.items.find(i=>i.type==='spell' && i.system.activities.some(a=>a.damage?.parts?.length));
    const activity = item.system.activities.find(a=>a.damage?.parts?.length);
    const flags = foundry.utils.deepClone(item._source.flags);
    let rolls;
    try {rolls = await activity.rollDamage({}, {configure:false}, {create:false});}
    finally {await item.update({flags}, {recursive:false, diff:false});}
    if (!rolls?.length) throw Error('Missing spell damage rolls');
    return {item:item.name,rolls:rolls.map(r=>({formula:r.formula,total:r.total}))};
  });
  await check('Encounter table evaluation', async () => {
    const pack = game.packs.get('dnd-tomb-annihilation.tables');
    const index = await pack.getIndex();
    const entry = index.find(e=>/encuentro/i.test(e.name));
    if (!entry) throw Error('No encounter table');
    const table = await pack.getDocument(entry._id);
    const result = await table.roll();
    if (!result.results.length) throw Error('No encounter result');
    return {table:table.name,results:result.results.map(r=>r.text ?? r.description),total:result.roll.total};
  });
  console.log('TOA_AUTOMATION_RESULT '+JSON.stringify(report));
  ui.notifications.info(`Automatizaciones: ${report.checks.length} comprobaciones correctas; ${report.errors.length} errores.`);
  return report;
}
