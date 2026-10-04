import os

filepath = 'crm.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('class="cs-slide-banner fade-in-section"', 'class="cs-slide-banner crm-banner fade-in-section"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
