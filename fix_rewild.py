import os

filepath = 'rewild.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('bar.jpg', 'bar.webp')
content = content.replace('dj.jpg', 'dj.webp')
content = content.replace('caccia-al-tesoro.jpg', 'caccia-al-tesoro.webp')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
