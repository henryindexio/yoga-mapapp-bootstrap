import pickle
import os
import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
from bokeh.io import output_file, show, curdoc
from bokeh.models import ColumnDataSource, GMapOptions, TextInput, Button, HoverTool
from bokeh.layouts import row, column, widgetbox
from bokeh.plotting import gmap
from bokeh.embed import components, server_document
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():

    script = server_document(url = "https://yoga-mapapp.herokuapp.com/mapapp")

    return render_template('index.html', the_script=script)

def update():
    
    InputZipcode = text_input.value

if __name__ == '__main__':
    app.run(debug=True)
    
