import markdown
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(Path('templates')))
tpl = env.get_template('page.html')

md_root = Path('md')
top_level_dirs = [p.name for p in md_root.iterdir() if p.is_dir()]

inpaths = list(md_root.glob('**/*.md'))
for inpath in inpaths:
    outpath = Path('build') / inpath.relative_to('md').with_suffix('.html')
    os.makedirs(outpath.parent, exist_ok=True)
    if inpath.name == "index.md":
        sublinks = [
            (p.relative_to('md').with_suffix('.html'), p.with_suffix('').name)
            for p in inpaths if p.parent == inpath.parent and p.name != "index.md"
        ]
    else:
        sublinks = []
    with open(inpath) as infile, open(outpath, 'w') as outfile:
        md_content = infile.read()
        html_content = markdown.markdown(md_content, output_format='html5')
        outfile.write(
            tpl.render(
                links=top_level_dirs,
                content=html_content,
                sublinks=sublinks
            )
        )
