# Tomb of Annihilation — Text only — Spanish Translation

[Español](README.md) | **English**

Translation for Foundry VTT using Babele. Module ID: `translate-dnd5e-tomb-annihilation-es`.

## Status

Version: **0.2.0**. Text-only test variant. Includes five compendiums and 126 interface keys. Project reports record the textual review as closed; complete functional validation remains pending. The package replaces 47 Spanish image paths with paths from the official module and does not include images. Labels within those images remain in their original language.

See [CHANGELOG.md](CHANGELOG.md).

## Requirements

Versions declared in the manifest; “—” means that the corresponding limit is not declared.

| Dependency | Minimum | Verified |
|---|---|---|
| Foundry VTT | 14.368 | 14.368 |
| dnd5e | 6.0.3 | 6.0.3 |
| babele | 2.9.1 | — |
| dnd-tomb-annihilation | 2.0.0 | — |

Install and enable the dependencies, purchasing official products separately when required.

Before importing, disable Babele’s **Sync imported Adventure token names**. Full and text-only variants share the same ID; do not install them as separate modules. Use a fresh import in a test world to check this variant. Rebuilding the full variant requires Spanish assets that are not versioned in this clone.

## Installation

In Foundry's Setup screen, open **Add-on Modules → Install Module** and use this manifest:

```text
https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/releases/latest/download/module.json
```

For manual installation, download `translate-dnd5e-tomb-annihilation-es.zip` from [releases](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/releases). With Foundry stopped, extract the `translate-dnd5e-tomb-annihilation-es` folder into `Data/modules/`; the manifest must be at `Data/modules/translate-dnd5e-tomb-annihilation-es/module.json`.

## Activation

1. Open a dnd5e world.
2. Enable Babele, its dependencies, the required official products and this translation.
3. Select **Spanish** and reload the world.
4. Open a translated compendium to check the result.

Registration is automatic for `es` and its regional variants. Other languages do not enable the Spanish translation.

## Updating

Update through Foundry or replace the folder with the published ZIP while Foundry is stopped. Reload the world. Previously imported copies do not synchronize automatically: review differences before replacing documents with your own changes.

## Included content

- `dnd-tomb-annihilation.actors.json`.
- `dnd-tomb-annihilation.adventures.json`.
- `dnd-tomb-annihilation.items.json`.
- `dnd-tomb-annihilation.macros.json`.
- `dnd-tomb-annihilation.tables.json`.

## Limitations

Text coverage and automated tests do not establish that every gameplay automation works. Observe the limitations listed under Status. Imported copies do not update automatically. New release URLs require a publication containing their assets; until available, use a validated ZIP. Private sources, PDFs, OCR and complete official exports are not distributed.

## Support and contributions

Report problems in [issues](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/issues), including versions, affected compendium/document, steps, expected and observed results, and whether it is an imported copy.

## Development

The [development guide](https://github.com/foundryvtt-sinregistrar/translate-dnd5e-tomb-annihilation-es/blob/main/DEVELOPER.md) is available in the repository and excluded from the installable ZIP.

## License and credits

Original contributions by `foundryvtt-sinregistrar` are available under the [MIT license](LICENSE.md), within the scope stated there. The translated source content and other third-party materials retain their rights and terms; MIT grants no additional permissions over them.

Unofficial translation, not affiliated with Wizards of the Coast or Foundry VTT. Official product materials belong to their respective owners. Module author: [foundryvtt-sinregistrar](https://github.com/foundryvtt-sinregistrar).
