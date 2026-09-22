// Execute validateRuntime() from a GM script macro. No source packs are modified.
const MODULE = "translate-dnd5e-tomb-annihilation-es";
const ROOT = `/modules/${MODULE}`;
const PACKS = ["adventures", "actors", "items", "tables", "macros"];
const json = async path => {
  const response = await fetch(`${ROOT}/${path}`, {cache: "no-store"});
  if (!response.ok) throw new Error(`${path}: ${response.status}`);
  return response.json();
};

export async function validateRuntime({importPilot = false} = {}) {
  if (!game.user.isGM || !game.babele) throw new Error("A GM session with Babele is required.");
  const {MappedCompendium} = await import("/modules/babele/script/compendium/mapped-compendium.js");
  const {DocumentMappings} = await import("/modules/babele/script/mapping/document-mappings.js");
  const {ConverterRegistry} = await import("/modules/babele/script/converter/converter-registry.js");
  const custom = await import(`${ROOT}/scripts/converters/toa-merge-by-id.js?revision=2`);
  const registry = new ConverterRegistry({...game.babele.converterRegistry.snapshot(), ...custom});
  const mappings = new DocumentMappings(game.babele.documentMappings.current(), {
    identityExtractors: game.babele.documentMappings.identityExtractors,
    converterRegistry: registry
  });
  const report = {date:new Date().toISOString(), foundry:game.version, system:game.system.version,
    babele:game.modules.get("babele").version, activeSession:!!game.modules.get(MODULE)?.active,
    checks:[], errors:[], imports:[]};
  const pilot = [];
  for (const name of PACKS) {
    const collection = `dnd-tomb-annihilation.${name}`;
    const source = await json(`dev-tools/export/data/${collection}.en.json`);
    const translation = await json(`compendium/${collection}.json`);
    const mapped = new MappedCompendium({id:collection, name, type:source.documentType,
      packageName:"dnd-tomb-annihilation", packageType:"module"}, translation, {documentMappings:mappings, language:"es"});
    const documents = [];
    const rawDocuments = [];
    for (const original of source.documents) {
      try {
        const translated = report.activeSession ? game.babele.translate(collection, original) : mapped.translate(original);
        rawDocuments.push(foundry.utils.deepClone(translated));
        if (translated.name !== translation.entries[original._id].name) throw new Error("Root name was not translated");
        // Construct documents through Foundry's real schema without saving them.
        const cls = getDocumentClass(source.documentType);
        const document = new cls(translated, {pack:collection});
        document.validate({strict:true});
        documents.push(document.toObject());
        report.checks.push({collection,id:original._id,name:document.name});
        if (source.documentType === "Adventure") {
          pilot.push(["JournalEntry", document.toObject().journal.find(d => d._id === "toaCh2AldaniBasi")]);
          pilot.push(["Scene", document.toObject().scenes.find(d => d._id === "toaAtaazMuhahah0")]);
        }
        if (["vStrC3BjGho0xSsc", "0AdOEoqkCYgxTld8", "toaCh4YuantiMali"].includes(original._id)) {
          pilot.push([source.documentType, document.toObject()]);
        }
      } catch (error) { report.errors.push({collection,id:original._id,error:error.message}); }
    }
    await write(`${collection}.validated.json`, {collection, documents});
    await write(`${collection}.translated.json`, {collection, documents:rawDocuments});
  }
  if (importPilot) {
    if (!report.activeSession) throw new Error("Activate the translation before importing the pilot.");
    for (const [type, data] of pilot) {
      if (!data) throw new Error(`Missing pilot ${type}`);
      const sourceId = data._id;
      const collection = game.collections.get(type);
      let imported = collection.find(d => d.getFlag(MODULE, "pilotSource") === sourceId);
      if (!imported) {
        let folder = game.folders.find(f => f.type === type && f.name === "ToA — Pruebas de traducción");
        if (!folder) folder = await Folder.create({name:"ToA — Pruebas de traducción",type});
        const copy = foundry.utils.deepClone(data);
        delete copy._id;
        copy.folder = folder.id;
        copy.flags ??= {};
        copy.flags[MODULE] = {pilotSource:sourceId};
        if (type === "Scene") { copy.active = false; copy.navigation = false; }
        imported = await getDocumentClass(type).create(copy, {renderSheet:false});
      }
      if (imported.name !== data.name) throw new Error(`Pilot import name mismatch: ${type}`);
      report.imports.push({type,id:imported.id,name:imported.name,sourceId});
    }
  }
  await write("toa-runtime-validation.json", report);
  ui.notifications.info(`ToA: ${report.checks.length} documentos validados; ${report.errors.length} errores.`);
  return report;
}

async function write(name, data) {
  const result = await foundry.applications.apps.FilePicker.upload("data", `modules/${MODULE}/dev-tools/export/data`,
    new File([JSON.stringify(data,null,2)+"\n"],name,{type:"application/json"}), {}, {notify:false});
  if (!result?.path) throw new Error(`Failed to save ${name}`);
}
