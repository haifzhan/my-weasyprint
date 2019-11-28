from os import path, walk
from flask import Flask, render_template, url_for
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

TEMPLATE_NAME = 'web_template.html'

# Display Web View
@app.route('/my-report/', defaults={'name': 'World'})
def ticket_html(name):
    return render_template(TEMPLATE_NAME, name=name, assets_dir="http://localhost:8080")


# Generate PDF Version
@app.route('/my-report.pdf')
def ticket_pdf():
    # Make a PDF straight from HTML in a string.
    html = render_template(TEMPLATE_NAME, assets_dir="http://localhost:8080")
    return render_pdf(HTML(string=html))