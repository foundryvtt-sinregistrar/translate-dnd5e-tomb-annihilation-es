/** Keep reviewed scene labels after Babele's asynchronous actor-name sync. */
export async function restoreAdventureLabels(adventure, result) {
  let written = 0;
  for (const scene of [...(result.created?.Scene ?? []), ...(result.updated?.Scene ?? [])]) {
    const original = Array.from(adventure.scenes).find(s => s._id === scene.id);
    if (!original) continue;
    const updates = [];
    for (const token of scene.tokens) {
      const name = original.tokens.find(t => t._id === token.id)?.name;
      // The old name may still be visible while Babele's write is in flight.
      if (typeof name === 'string') updates.push({_id:token.id, name});
    }
    if (updates.length) {
      // Force the final write even when the current name still matches.
      await scene.updateEmbeddedDocuments('Token', updates, {diff:false});
      written += updates.length;
    }
  }
  return written;
}

export function configureAdventureImport(adventure, options) {
  if (adventure.pack !== 'dnd-tomb-annihilation.adventures') return;
  if (game.settings.get('core', 'language')?.split('-')[0].toLowerCase() !== 'es') return;
  options.postImport ??= [];
  options.postImport.push(function (result) { return restoreAdventureLabels(this, result); });
}

if (typeof Hooks !== 'undefined') Hooks.on('preImportAdventure', configureAdventureImport);
