import re

with open('giardini.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = r'<div class="cs-banner">\s*<div class="cs-banner-bg" style="background-image: url\(\'(.*?)\'\);">\s*<div class="cs-banner-overlay"></div>\s*</div>\s*<div class="cs-banner-content">\s*<div class="cs-banner-text">(.*?)</div>\s*</div>\s*</div>'

def replacement(match):
    img_url = match.group(1)
    text = match.group(2)
    return f'''<div class="cs-slide-banner">
            <img src="{img_url}" alt="Slide" class="cs-slide-img">
            <div class="cs-slide-text">{text}</div>
        </div>'''

new_html = re.sub(pattern, replacement, html)

with open('giardini.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

css_code = '''
/* Hybrid Slide Banner for Giardini */
.cs-slide-banner {
    margin: 60px auto;
    text-align: center;
}
.cs-slide-img {
    max-width: 900px;
    width: 100%;
    margin: 0 auto;
    display: block;
    border-radius: var(--radius);
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}
.cs-slide-text {
    display: none;
}

@media (max-width: 768px) {
    .cs-slide-banner {
        background-color: var(--bg-white);
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        margin: 50px 0;
        text-align: left;
    }
    .cs-slide-img {
        border-radius: 0;
        box-shadow: none;
        max-width: 100%;
        width: 100%;
        height: 250px;
        object-fit: cover;
    }
    .cs-slide-text {
        display: block;
        padding: 25px;
        background-color: white;
        color: var(--text-dark);
        font-size: 1.15rem;
        font-weight: 600;
        font-family: 'Outfit', sans-serif;
    }
}
'''

with open('rewild.css', 'a', encoding='utf-8') as f:
    f.write(css_code)
