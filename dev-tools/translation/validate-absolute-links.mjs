// Resolve absolute UUID/Embed targets and verify heading anchors in translated packs.
// Relative UUIDs and item commands require their own context checks.
export async function validateAbsoluteLinks() {
  if (!game.user.isGM || game.world.title !== 'DnD5e-6.0.3-Testing-Clean') throw Error('Clean test world required');
  const targets = new Map();
  function visit(value, path) {
    if (typeof value === 'string') {
      for (const match of value.matchAll(/@(?:UUID|Embed)\[([^\]\s]+)/g)) {
        const uuid = match[1];
        if (!/^(?:Compendium|Actor|Item|JournalEntry|Scene|RollTable|Macro)\./.test(uuid)) continue;
        if (!targets.has(uuid)) targets.set(uuid, []);
        targets.get(uuid).push(path);
      }
    } else if (value && typeof value === 'object') {
      for (const [key, child] of Object.entries(value)) visit(child, `${path}.${key}`);
    }
  }
  for (const pack of ['actors','adventures','items','macros','tables']) {
    const response = await fetch(`/modules/translate-dnd5e-tomb-annihilation-es/compendium/dnd-tomb-annihilation.${pack}.json`, {cache:'no-store'});
    if (!response.ok) throw Error(`Cannot read ${pack}`);
    visit(await response.json(), pack);
  }
  const report = {date:new Date().toISOString(),world:game.world.title,unique:targets.size,resolved:0,missing:[]};
  const entries = [...targets];
  for (let offset=0; offset<entries.length; offset+=10) {
    await Promise.all(entries.slice(offset,offset+10).map(async ([uuid,fields]) => {
      try {
        const [base, anchor] = uuid.split('#');
        const document = await fromUuid(base);
        const toc = document && anchor ? JournalEntryPage.buildTOC(new DOMParser().parseFromString(document.text?.content ?? '', 'text/html').body, {includeElement:false}) : null;
        if (document && (!anchor || Object.hasOwn(toc, anchor))) report.resolved++;
        else report.missing.push({uuid,occurrences:fields.length,field:fields[0]});
      } catch (error) {report.missing.push({uuid,occurrences:fields.length,field:fields[0],error:String(error)});}
    }));
  }
  report.missing.sort((a,b)=>a.uuid.localeCompare(b.uuid));
  console.log('TOA_ABSOLUTE_LINKS '+JSON.stringify(report));
  return report;
}
