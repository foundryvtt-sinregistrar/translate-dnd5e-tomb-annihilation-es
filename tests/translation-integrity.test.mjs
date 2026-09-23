import assert from "node:assert/strict";
import {test} from "node:test";
import {readFileSync, existsSync} from "node:fs";
import {createHash} from "node:crypto";
import {toaFolderNamesById, toaJournalPagesById, toaAdventureActorsById} from "../scripts/converters/toa-merge-by-id.js";

test("Adventure actors preserve explicit proper names and embedded biography references", () => {
  globalThis.foundry = {utils:{deepClone:structuredClone, setProperty(object,path,value) {
    const keys=path.split('.'); const last=keys.pop();
    for (const key of keys) object=object[key] ??= {};
    object[last]=value;
  }}};
  const source=[{_id:"npc",name:"Voltan",prototypeToken:{name:"Voltan"},
    system:{details:{biography:{value:"@Embed[JournalEntry.guide]"}},attributes:{hp:{value:25}}}}];
  const patch={npc:{name:"Voltan",tokenName:"Voltan",biography:"@Embed[JournalEntry.guide]"}};
  assert.deepEqual(toaAdventureActorsById(source,patch),source);
  assert.notEqual(toaAdventureActorsById(source,patch),source);
  delete globalThis.foundry;
});

test("Adventure folders use IDs, including duplicate source names", () => {
  globalThis.foundry = {utils:{deepClone:structuredClone}};
  const original = [{_id:"one",name:"Chapter",folder:null},{_id:"two",name:"Chapter",folder:"one"}];
  const result = toaFolderNamesById(original,{one:"Capítulo 1",two:"Capítulo 2",missing:"Ausente"});
  assert.deepEqual(result,[{_id:"one",name:"Capítulo 1",folder:null},{_id:"two",name:"Capítulo 2",folder:"one"}]);
  assert.equal(original[0].name,"Chapter");
  delete globalThis.foundry;
});

test("Journal translation preserves page identity, format, image and ordering", () => {
  globalThis.foundry = {utils:{deepClone:structuredClone}};
  const original = [{_id:"page",name:"Name",sort:100,type:"text",text:{format:1,content:"English"},image:{src:"original.webp"}}];
  const result = toaJournalPagesById(original,{page:{name:"Nombre",text:"Español"},other:{text:"No insertar"}});
  assert.deepEqual(result,[{...original[0],name:"Nombre",text:{format:1,content:"Español"}}]);
  assert.equal(original[0].text.content,"English");
  delete globalThis.foundry;
});

const englishUI = new URL("../../dnd-tomb-annihilation/lang/en.json",import.meta.url);
test("Spanish handouts preserve page identity and replace only registered image pages", () => {
  globalThis.foundry = {utils:{deepClone:structuredClone}};
  try {
    const manifest=JSON.parse(readFileSync(new URL('../dev-tools/translation/handout-assets.json',import.meta.url),'utf8'));
    const adventure=JSON.parse(readFileSync(new URL('../compendium/dnd-tomb-annihilation.adventures.json',import.meta.url),'utf8'));
    const patches=adventure.entries[manifest.adventureId].journals[manifest.journalId].pages;
    for (const asset of manifest.assets) {
      const original={_id:asset.pageId,type:'image',src:asset.source,sort:17,image:{caption:'English'}};
      const result=toaJournalPagesById([original],patches)[0];
      assert.equal(result.src,asset.translation);
      assert.equal(result._id,original._id);
      assert.equal(result.sort,original.sort);
      assert.equal(original.src,asset.source);
      const path=asset.translation.replace('modules/translate-dnd5e-tomb-annihilation-es/','../');
      assert.equal(createHash('sha256').update(readFileSync(new URL(path,import.meta.url))).digest('hex'),asset.sha256);
    }
    const unmodified={_id:'untouched',type:'image',src:'original.webp'};
    const text={_id:'text',type:'text',src:null};
    assert.deepEqual(toaJournalPagesById([unmodified,text],{text:{src:'wrong.jpg'}}),[unmodified,text]);
  } finally { delete globalThis.foundry; }
});

test("Spanish UI covers the official keys and preserves formatting placeholders", {skip:!existsSync(englishUI)}, () => {
  const english = JSON.parse(readFileSync(englishUI,"utf8"));
  const spanish = JSON.parse(readFileSync(new URL("../lang/es.json",import.meta.url),"utf8"));
  let count = 0;
  function check(source,target,path) {
    assert.deepEqual(Object.keys(target).sort(),Object.keys(source).sort(),path);
    for (const [key,value] of Object.entries(source)) {
      if (typeof value === "object") check(value,target[key],`${path}.${key}`);
      else {
        assert.equal(typeof target[key],"string");
        assert.ok(target[key].trim());
        assert.deepEqual(target[key].match(/\{[^}]+\}/g) ?? [],value.match(/\{[^}]+\}/g) ?? [],key);
        count++;
      }
    }
  }
  check(english,spanish,"UI");
  assert.ok(count > 100);
});
