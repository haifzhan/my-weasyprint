# How to run as a python program?
comment out style.css when run as a python program `<link rel=stylesheet href="{{ url_for('static', filename='css/style.css') }}" />`
1. Go to plotly folder generate line chart by calling `python line_chart.py`
2. Run `python driver.py` generate PDF report


# How to run as a Flask app?

import style.css when use flask:
 `<link rel=stylesheet href="{{ url_for('static', filename='css/style.css') }}" />`

 step1: `export FLASK_APP=flask_driver.py`
 step2: `flask run`