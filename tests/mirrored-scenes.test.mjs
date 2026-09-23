import test from 'node:test';
import assert from 'node:assert/strict';
import {MIRRORED_SCENE_IDS, mirroredScenePairs} from '../scripts/mirrored-scenes.mjs';

test('finds all six mirrored scenes after translation or manual renaming', () => {
  const originals = new Map(MIRRORED_SCENE_IDS.map(id => [id, {id, name: 'Nivel reflejado'}]));
  const scenes = new Map(MIRRORED_SCENE_IDS.map(id => [id, {id, name: 'Nombre personalizado'}]));
  const pairs = mirroredScenePairs({scenes: originals}, scenes);
  assert.equal(pairs.length, 6);
  for (const pair of pairs) assert.equal(pair.original.id, pair.scene.id);
});

test('refuses an incomplete import before resetting any scene', () => {
  const scenes = new Map(MIRRORED_SCENE_IDS.map(id => [id, {id}]));
  const incomplete = new Map(scenes);
  incomplete.delete(MIRRORED_SCENE_IDS[5]);
  assert.throws(() => mirroredScenePairs({scenes}, incomplete), /toaMirroredLvl60/);
});
