import glob
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.tags = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.tags.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag not in self.void_elements:
            if not self.tags:
                print(f"Error in {self.filename}: unexpected end tag </{tag}> at line {self.getpos()[0]}")
            else:
                last_tag, pos = self.tags.pop()
                if last_tag != tag:
                    print(f"Error in {self.filename}: mismatched tag. Expected </{last_tag}> (from line {pos[0]}), got </{tag}> at line {self.getpos()[0]}")

for f in glob.glob('*.html'):
    parser = MyHTMLParser(f)
    with open(f, 'r', encoding='utf-8') as file:
        parser.feed(file.read())
    if parser.tags:
        print(f"Warning in {f}: unclosed tags: {[t[0] for t in parser.tags]}")
print('Validation complete.')
