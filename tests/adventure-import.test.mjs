import {test} from 'node:test';
import assert from 'node:assert/strict';
import {restoreAdventureLabels, configureAdventureImport} from '../scripts/adventure-import.mjs';

test('preserves reviewed labels when Babele has a generic name update in flight', async () => {
  const token = {id:'t',name:'Nephyr'};
  const synchronization = Promise.resolve().then(() => { token.name = 'Aarakocra'; });
  const writes = [];
  const scene = {id:'s',tokens:[token,{id:'u',name:'Untouched'}],
    updateEmbeddedDocuments:async (type,updates,options) => {
      assert.equal(options.diff,false, 'Equal current values must still be written');
      await synchronization;
      writes.push({type,updates});
      for (const update of updates) token.name = update.name;
    }};
  const adventure = {scenes:[{_id:'s',tokens:[{_id:'t',name:'Nephyr'}]}]};
  assert.equal(await restoreAdventureLabels(adventure,{created:{Scene:[scene]}}),1);
  assert.equal(token.name,'Nephyr');
  assert.deepEqual(writes,[{type:'Token',updates:[{_id:'t',name:'Nephyr'}]}]);
  assert.equal(await restoreAdventureLabels(adventure,{updated:{}}),0);
});

test('handles updated scenes and ignores scenes outside the adventure', async () => {
  const writes = [];
  const scene = {id:'s',tokens:[{id:'t',name:'Bandido'}],
    updateEmbeddedDocuments:async (type,updates) => writes.push(updates)};
  const other = {id:'other',tokens:[{id:'t',name:'Keep'}]};
  const adventure = {scenes:[{_id:'s',tokens:[{_id:'t',name:'Pirata'}]}]};
  assert.equal(await restoreAdventureLabels(adventure,{updated:{Scene:[scene,other]}}),1);
  assert.deepEqual(writes,[[{_id:'t',name:'Pirata'}]]);
});

test('registers restoration only for Spanish Tomb of Annihilation imports', () => {
  globalThis.game = {settings:{get:()=> 'en'}};
  const options = {};
  configureAdventureImport({pack:'dnd-tomb-annihilation.adventures'},options);
  assert.equal(options.postImport,undefined);
  game.settings.get = ()=> 'es-ES';
  configureAdventureImport({pack:'other'},options);
  assert.equal(options.postImport,undefined);
  configureAdventureImport({pack:'dnd-tomb-annihilation.adventures'},options);
  assert.equal(options.postImport.length,1);
  delete globalThis.game;
});
