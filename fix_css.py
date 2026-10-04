import os

filepath = 'rewild.css'
with open(filepath, 'rb') as f:
    content = f.read()

# Try to decode safely, removing the bad append
try:
    content_str = content.decode('utf-8', errors='ignore')
except:
    pass

# Remove the bad part
import re
content_str = re.sub(r'[\x00]', '', content_str)
content_str = re.sub(r'@media \(max-width: 768px\) \{\s*\.crm-banner .*\}\s*\}\s*$', '', content_str, flags=re.DOTALL)

# Append properly
content_str += '''
@media (max-width: 768px) {
    .crm-banner .cs-slide-img {
        height: auto !important;
        max-height: 85vh;
        object-fit: contain !important;
        background-color: #f9fafb;
    }
}
'''

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content_str.strip() + '\n')
