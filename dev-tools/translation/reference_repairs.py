"""Explicit, field-scoped corrections to confirmed broken original references."""
def apply_reference_repairs(text, key, repairs):
    for rule in repairs.get(key, []):
        if rule['source'] not in text:
            raise ValueError(f'Stale reference repair: {key}: {rule["source"]}')
        text=text.replace(rule['source'],rule['translation'])
    return text
