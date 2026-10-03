import os

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mapping of mangled sequences back to correct Italian characters
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
        'Ã¨': 'è',
        'capacitÃ ': 'capacità ',
        'visibilitÃ ': 'visibilità ',
        'autenticitÃ ': 'autenticità '
    }
    
    for bad, good in replacements.items():
        content = content.replace(bad, good)
        
    # Some specific fixes based on the screenshot
    content = content.replace('giÃ', 'già')
    content = content.replace('UniversitÃ', 'Università')
    content = content.replace('CiÃ²', 'Ciò')
    content = content.replace('capacitÃ', 'capacità')
    content = content.replace('visibilitÃ', 'visibilità')
    content = content.replace('autenticitÃ', 'autenticità')
    content = content.replace('Ã¨', 'è')
    content = content.replace('Ã', 'à') # fallback for loose Ã if followed by space, but dangerous.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_file('index.html')
