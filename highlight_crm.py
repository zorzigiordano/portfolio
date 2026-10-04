import re

filepath = 'crm.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Helper to wrap in strong and span
def wrap(match):
    text = match.group(0)
    return f'<strong><span style="color: var(--primary-color);">{text}</span></strong>'

# 1. "corso di CRM e Marketing Automation"
html = re.sub(r'corso di CRM e Marketing Automation', wrap, html)

# 2. "project work"
html = re.sub(r'project work', wrap, html)

# 3. "gestione manuale dei candidati esclusi"
html = re.sub(r'gestione manuale dei candidati esclusi', wrap, html)

# 4. remove bold from "gestione frammentata dei dati"
# It is currently: <strong>gestione frammentata dei dati</strong>
html = html.replace('<strong>gestione frammentata dei dati</strong>', 'gestione frammentata dei dati')

# 5. "regole tracciati d'importazione"
# wait, in Italian it's "regole dei tracciati d'importazione", the user said "regole tracciati d'importazione". I'll just find what's there.
html = re.sub(r'regole dei tracciati d\'importazione', wrap, html)
if 'regole tracciati d\'importazione' in html:
    html = re.sub(r'regole tracciati d\'importazione', wrap, html)

# 6. "workflow automatizzato"
# It is already <strong>workflow automatizzato</strong> in the original text, let's replace it with the span version
html = html.replace('<strong>workflow automatizzato</strong>', 'workflow automatizzato') # remove old bold first
html = re.sub(r'workflow automatizzato', wrap, html)

# 7. "mailchimp" (ignore case for matching, but keep original case in replacement)
def wrap_mailchimp(match):
    return f'<strong><span style="color: var(--primary-color);">{match.group(0)}</span></strong>'
html = re.sub(r'(?i)\bmailchimp\b', wrap_mailchimp, html)

# 8. "digital strategist a 360°"
html = re.sub(r'digital strategist a 360(?:°||Â°)', wrap_mailchimp, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
