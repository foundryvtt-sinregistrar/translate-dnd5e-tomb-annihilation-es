export function mergeById(source, translation) {
  if (!source || typeof source !== "object" || !translation || typeof translation !== "object") {
    return source;
  }

  const out = foundry.utils.deepClone(source);
  for (const [id, patch] of Object.entries(translation)) {
    if (!patch || typeof patch !== "object") continue;

    if (Array.isArray(out)) {
      const target = out.find((row) => (row?._id ?? row?.id) === id);
      if (target) foundry.utils.mergeObject(target, patch, { insertKeys: true, overwrite: true, inplace: true });
      continue;
    }

    if (out[id]) {
      foundry.utils.mergeObject(out[id], patch, { insertKeys: true, overwrite: true, inplace: true });
    }
  }
  return out;
}

export const toaActivitiesById = mergeById;
export const toaEffectsById = mergeById;
export const toaAdvancementById = mergeById;
export const toaTableResultsById = mergeById;
export const toaSceneTextById = mergeById;

export function toaFolderNamesById(source, translation) {
  if (!Array.isArray(source) || !translation || typeof translation !== "object") return source;
  const out = foundry.utils.deepClone(source);
  for (const folder of out) {
    const name = translation[folder._id ?? folder.id];
    if (typeof name === "string") folder.name = name;
  }
  return out;
}

// Adventure copies must use their own text even when it equals the English
// source (proper names and @Embed references). Generic Babele fallback can
// otherwise replace them with a different creature's name or biography.
export function toaAdventureActorsById(source, translation) {
  if (!Array.isArray(source) || !translation || typeof translation !== "object") return source;
  const out = foundry.utils.deepClone(source);
  const paths = {
    name:"name", tokenName:"prototypeToken.name", biography:"system.details.biography.value",
    biographyPublic:"system.details.biography.public", alignment:"system.details.alignment",
    creatureType:"system.details.type.custom", creatureSubtype:"system.details.type.subtype",
    languages:"system.traits.languages.custom", senses:"system.attributes.senses.special"
  };
  for (const actor of out) {
    const patch = translation[actor._id ?? actor.id];
    if (!patch || typeof patch !== "object") continue;
    for (const [key,path] of Object.entries(paths)) {
      if (typeof patch[key] === "string") foundry.utils.setProperty(actor,path,patch[key]);
    }
    if (patch.items) actor.items = toaActorItemsById(actor.items,patch.items);
    if (patch.effects) actor.effects = mergeById(actor.effects,patch.effects);
  }
  return out;
}

export function toaSceneTokensById(source, translation) {
  if (!Array.isArray(source) || !translation || typeof translation !== "object") return source;
  const out = foundry.utils.deepClone(source);
  for (const token of out) {
    const patch = translation[token._id ?? token.id];
    if (!patch || typeof patch !== "object") continue;
    if (typeof patch.name === "string") token.name = patch.name;
    if (patch.delta && token.delta) {
      const id = token.delta._id ?? token.delta.id;
      if (id) token.delta = toaAdventureActorsById([token.delta], {[id]:patch.delta})[0];
    }
  }
  return out;
}

export function toaJournalPagesById(source, translation) {
  if (!source || !translation || typeof translation !== "object") return source;
  const out = foundry.utils.deepClone(source);
  const pages = Array.isArray(out) ? out : Array.from(out?.contents ?? Object.values(out));
  for (const page of pages) {
    const id = page?._id ?? page?.id;
    const patch = id ? translation[id] : null;
    if (!patch || typeof patch !== "object") continue;
    if (typeof patch.name === "string") page.name = patch.name;
    if (page.type === "image" && typeof patch.src === "string") page.src = patch.src;
    if (typeof patch.image?.caption === "string") {
      page.image ??= {};
      page.image.caption = patch.image.caption;
    }
    if (typeof patch.text === "string") {
      if (typeof page.text === "string") page.text = patch.text;
      else {
        page.text ??= {};
        page.text.content = patch.text;
        page.text.format ??= 1;
      }
    }
  }
  return out;
}

export function toaActorItemsById(source, translation) {
  if (!Array.isArray(source) || !translation || typeof translation !== "object") return source;

  const out = foundry.utils.deepClone(source);
  for (const item of out) {
    const id = item?._id ?? item?.id;
    const patch = id ? translation[id] : null;
    if (!patch || typeof patch !== "object") continue;

    if (typeof patch.name === "string") item.name = patch.name;
    if (typeof patch.description === "string") {
      item.system ??= {};
      item.system.description ??= {};
      item.system.description.value = patch.description;
    }
    if (typeof patch.descriptionChat === "string") {
      item.system ??= {}; item.system.description ??= {};
      item.system.description.chat = patch.descriptionChat;
    }
    if (typeof patch.requirements === "string") {
      item.system ??= {};
      item.system.requirements = patch.requirements;
    }
    if (typeof patch.unidentifiedDescription === "string") {
      item.system ??= {}; item.system.unidentified ??= {};
      item.system.unidentified.description = patch.unidentifiedDescription;
    }
    if (patch.activities) {
      item.system ??= {};
      item.system.activities = mergeById(item.system.activities ?? {}, patch.activities);
    }
    if (patch.effects) item.effects = mergeById(item.effects ?? [], patch.effects);
    if (patch.advancement) {
      item.system ??= {};
      item.system.advancement = mergeById(item.system.advancement ?? [], patch.advancement);
    }
  }
  return out;
}
