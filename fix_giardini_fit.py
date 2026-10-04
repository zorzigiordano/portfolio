import os
import re

# 1. Update CSS
css_file = 'rewild.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()
css = css.replace('.crm-banner .cs-slide-img {', '.crm-banner .cs-slide-img,\n    .fit-banner .cs-slide-img {')
with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update giardini.html
html_file = 'giardini.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find the specific slide banner that has giardini1.webp
# It looks like:
# <div class="cs-slide-banner">
#     <img src="materiale/giardini1.webp" ...

pattern = r'(<div class="cs-slide-banner">)(\s*<img src="materiale/giardini1.webp")'
html = re.sub(pattern, r'<div class="cs-slide-banner fit-banner">\2', html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
