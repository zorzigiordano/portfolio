import os
import re

for filepath in ['index.html', 'giardini.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    content = content.replace('giordano.png', 'giordano.webp')
    content = content.replace('giardini.jpg', 'giardini.webp')
    content = content.replace('giardini1.jpg', 'giardini1.webp')
    content = content.replace('giardini2.jpg', 'giardini2.webp')
    content = content.replace('giardini3.jpg', 'giardini3.webp')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
