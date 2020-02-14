# What to install?
install python3
```
conda install -c plotly plotly-orca
pip install plotly
pip install psutil
pip install WeasyPrint
pip install requests
```
# How to run as a python program?
comment out style.css when run as a python program `<link rel=stylesheet href="{{ url_for('static', filename='css/style.css') }}" />`
1. Go to plotly folder generate line chart by calling `python line_chart.py`
2. Run `python driver.py` generate PDF report


# How to run as a Flask app?

## Known issues

Images:
npm install -g http-server
goto assets folder and run `http-server ./`

import style.css when use flask:
 `<link rel=stylesheet href="{{ url_for('static', filename='css/style.css') }}" />`

 step1: `export FLASK_APP=flask_driver.py`
 step2: `flask run`