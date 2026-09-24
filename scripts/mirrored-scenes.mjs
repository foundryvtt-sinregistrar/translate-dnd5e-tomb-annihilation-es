// Stable scene IDs avoid the original macro's English-name lookup.
export const MIRRORED_SCENE_IDS = Object.freeze([
  'toaMirroredlvl10', 'toaMirroredlvl20', 'toaMirroredlvl30',
  'toaMirroredlvl40', 'toaMirroredlvl50', 'toaMirroredLvl60'
]);

export function mirroredScenePairs(adventure, scenes) {
  return MIRRORED_SCENE_IDS.map(id => {
    const original = Array.from(adventure.scenes.values()).find(scene => (scene.id ?? scene._id) === id);
    const scene = scenes.get(id);
    if (!original || !scene) throw new Error(`No se encuentra la escena reflejada ${id}`);
    return {original, scene};
  });
}

export async function resetMirroredScenes() {
  return foundry.applications.api.DialogV2.prompt({
    window: {title: 'Restablecer las escenas reflejadas'},
    content: '<p>¿Restablecer las seis escenas reflejadas? Se conservarán las fichas controladas por jugadores. Los demás elementos volverán a su estado original.</p>',
    ok: {
      label: 'Restablecer escenas',
      callback: async () => {
        const adventure = await fromUuid('Compendium.dnd-tomb-annihilation.adventures.Adventure.OQ0bB1QgjuxagwGI');
        // Validate every destination before modifying the first scene.
        const pairs = mirroredScenePairs(adventure, game.scenes);
        for (const {original, scene} of pairs) {
          const {drawings, lights, notes, regions, templates, tokens, walls} = original.toObject();
          const players = scene.tokens.filter(token => token.hasPlayerOwner).map(token => token.toObject());
          const playerIds = new Set(players.map(token => token._id));
          const restoredTokens = tokens.filter(token => !playerIds.has(token._id)).concat(players);
          await scene.update({drawings: [], lights: [], notes: [], regions: [], templates: [], tokens: [], walls: []},
            {recursive: false, diff: false});
          await scene.update({drawings, lights, notes, regions, templates, tokens: restoredTokens, walls});
        }
        ui.notifications.info('Escenas reflejadas restablecidas.');
      }
    },
    rejectClose: false
  });
}

export function installMirroredSceneCompatibility() {
  if (game.i18n.lang.split('-')[0] !== 'es') return false;
  const module = game.modules.get('dnd-tomb-annihilation');
  const macros = module?.macros;
  if (!macros?.ch5?.ar19) return false;
  // ES module namespace objects are read-only; preserve all sibling exports.
  module.macros = {...macros, ch5: {...macros.ch5,
    ar19: {...macros.ch5.ar19, resetMirroredScenes}}};
  return true;
}

if (typeof Hooks !== 'undefined') Hooks.once('ready', installMirroredSceneCompatibility);
