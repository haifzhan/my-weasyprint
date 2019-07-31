import os
import weasyprint
from jinja2 import Environment, FileSystemLoader

ROOT = '/Users/hzhang/google-drive/my-weasyprint'

TEMPLAT_SRC = os.path.join(ROOT, 'templates')
CSS_SRC = os.path.join(ROOT, 'static')
DEST_DIR = os.path.join(ROOT, 'output')

TEMPLATE = 'template.html'
CSS = 'styles.css'
OUTPUT_FILENAME = 'my-report.pdf'

def start():
    env = Environment(loader=FileSystemLoader(TEMPLAT_SRC))

    template = env.get_template(TEMPLATE)
    css = os.path.join(CSS_SRC, CSS)
    
    # variables
    template_vars = { }

    # rendering to html string
    rendered_string = template.render(template_vars)
    html = weasyprint.HTML(string=rendered_string)
    report = os.path.join(DEST_DIR, OUTPUT_FILENAME)
    html.write_pdf(report, stylesheets=[css])
    print('file is generated successfully')


if __name__ == '__main__':
    start()