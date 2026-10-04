import re

filepath = 'crm.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix alt tag
html = html.replace('alt="Mockup <strong><span style="color: var(--primary-color);">Mailchimp</span></strong> e Workflow"', 'alt="Mockup Mailchimp e Workflow"')

# Highlight "gestione completamente manuale dei candidati esclusi"
def wrap(match):
    text = match.group(0)
    return f'<strong><span style="color: var(--primary-color);">{text}</span></strong>'

html = re.sub(r'gestione completamente manuale dei candidati esclusi', wrap, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
