import os
import re
from pathlib import Path
import markdown

# Define paths
en_dir = Path("en")
pt_dir = Path("pt")
site_en_dir = Path("_site/en")
site_pt_dir = Path("_site/pt")

# Create directories if they don't exist
site_en_dir.mkdir(parents=True, exist_ok=True)
site_pt_dir.mkdir(parents=True, exist_ok=True)

def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown"""
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = match.group(2)
        return frontmatter, body
    return None, content

def parse_frontmatter(frontmatter):
    """Parse YAML frontmatter into a dictionary"""
    if not frontmatter:
        return {}
    
    data = {}
    for line in frontmatter.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip().strip('\'"')
    return data

def markdown_to_html(md_content):
    """Convert markdown to HTML"""
    return markdown.markdown(md_content, extensions=['extra', 'codehilite'])

def create_html_page(title, content, lang='en'):
    """Create a complete HTML page"""
    nav_links = {
        'en': '''
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <a class="navbar-brand" href="/">PlayData</a>
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="/editor">Try it</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/getting-started">Getting started</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/resource-cards">Resources</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/publications">Publications</a></li>
                <li class="nav-item"><a class="nav-link" href="/en/about">About</a></li>
            </ul>
        </nav>
        ''',
        'pt': '''
        <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
            <a class="navbar-brand" href="/">PlayData</a>
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="/editor">Teste</a></li>
                <li class="nav-item"><a class="nav-link" href="/pt/como-comecar">Começar</a></li>
                <li class="nav-item"><a class="nav-link" href="/pt/resource-cards">Recursos</a></li>
                <li class="nav-item"><a class="nav-link" href="/pt/publicacoes">Publicações</a></li>
                <li class="nav-item"><a class="nav-link" href="/pt/sobre">Sobre</a></li>
            </ul>
        </nav>
        '''
    }
    
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - PlayData</title>
    <link rel="stylesheet" href="/assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="/assets/css/beautifuljekyll.css">
    <link rel="stylesheet" href="/assets/css/bootstrap-social.css">
    <link rel="stylesheet" href="/assets/css/pygment_highlights.css">
</head>
<body>
    {nav_links.get(lang, nav_links['en'])}
    
    <div class="container" style="margin-top: 100px;">
        <div class="row">
            <div class="col-md-8 offset-md-2">
                <h1>{title}</h1>
                {content}
            </div>
        </div>
    </div>
    
    <footer class="footer">
        <div class="container">
            <p class="text-muted">PlayData © 2024</p>
        </div>
    </footer>
    
    <script src="/assets/js/bootstrap.min.js"></script>
    <script src="/assets/js/beautifuljekyll.js"></script>
</body>
</html>
"""
    return html

def process_markdown_file(filepath, site_dir, lang):
    """Process a markdown file and create HTML in _site"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    frontmatter, body = extract_frontmatter(content)
    fm_data = parse_frontmatter(frontmatter)
    
    # Get title
    title = fm_data.get('title', filepath.stem)
    
    # Convert markdown to HTML
    html_content = markdown_to_html(body)
    
    # Create full HTML page
    full_html = create_html_page(title, html_content, lang)
    
    # Create output path
    filename = filepath.stem
    output_dir = site_dir / filename
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "index.html"
    
    # Write HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    return str(output_file)

# Process English files
print("Building English pages...\n")
en_files = sorted(en_dir.glob('*.md'))
for en_file in en_files:
    try:
        output_path = process_markdown_file(en_file, site_en_dir, 'en')
        print(f"✓ Created: {output_path}")
    except Exception as e:
        print(f"✗ Error processing {en_file.name}: {e}")

# Process Portuguese files
print("\nBuilding Portuguese pages...\n")
pt_files = sorted(pt_dir.glob('*.md'))
for pt_file in pt_files:
    try:
        output_path = process_markdown_file(pt_file, site_pt_dir, 'pt')
        print(f"✓ Created: {output_path}")
    except Exception as e:
        print(f"✗ Error processing {pt_file.name}: {e}")

print("\nDone! Pages have been built and added to _site/")
