import os

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacements = {
        'Ã\xa0': 'à',
        'Ã¨': 'è',
        'Ã©': 'é',
        'Ã¬': 'ì',
        'Ã²': 'ò',
        'Ã¹': 'ù',
        'â€™': "'",
        'â€”': "—",
        'Â°': '°',
        'giÃ ': 'già ',
        'UniversitÃ ': 'Università ',
        'CiÃ²': 'Ciò',
        'capacitÃ ': 'capacità ',
        'visibilitÃ ': 'visibilità ',
        'autenticitÃ ': 'autenticità ',
        'identitÃ ': 'identità ',
        'socialitÃ ': 'socialità ',
        'qualitÃ ': 'qualità ',
        'PubblicitÃ ': 'Pubblicità ',
        'piÃ¹': 'più',
        'Ã\x83Â¨': 'è',
        '360Â°': '360°'
    }
    
    for bad, good in replacements.items():
        content = content.replace(bad, good)
        
    content = content.replace('giÃ', 'già')
    content = content.replace('UniversitÃ', 'Università')
    content = content.replace('CiÃ²', 'Ciò')
    content = content.replace('capacitÃ', 'capacità')
    content = content.replace('visibilitÃ', 'visibilità')
    content = content.replace('autenticitÃ', 'autenticità')
    content = content.replace('identitÃ', 'identità')
    content = content.replace('socialitÃ', 'socialità')
    content = content.replace('qualitÃ', 'qualità')
    content = content.replace('PubblicitÃ', 'Pubblicità')
    content = content.replace('piÃ¹', 'più')
    content = content.replace('Ã¨', 'è')
    content = content.replace('Ã²', 'ò')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for f in ['index.html', 'crm.html', 'giardini.html', 'rewild.html']:
    fix_file(f)
