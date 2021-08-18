from flask import Flask, render_template, session, redirect, url_for, flash, send_file, make_response, Response
from flask_sqlalchemy import SQLAlchemy


#Pandas and Matplotlib
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#other requirements
import io
import os
import sqlite3

basedir = os.path.abspath(os.path.dirname(__file__))

con = sqlite3.connect('fighter.sqlite')

df = pd.read_sql('SELECT * FROM fighter', con)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/database', methods=['GET', 'POST'])
def pandas():
    return render_template('database.html', PageTitle = "database", table=[df.to_html(classes='data', index = False)], titles= df.columns.values)

#Matplotlib page
@app.route('/matplot', methods=["POST", "GET"])
def mpl():
    return render_template('matplot.html', PageTitle = "Matplotlib")

@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = df.plot.scatter(x='weight (lbs)', y='height (in)').get_figure()
    return fig

@app.route('/plot2.png')
def plot2_png():
    fig2 = create_figure_2()
    output = io.BytesIO()
    FigureCanvas(fig2).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure_2():
    fig2 = df.plot.scatter(x="SubAvg", y="TDAvg").get_figure()
    return fig2

@app.route('/plot3.png')
def plot3_png():
    fig3 = create_figure_3()
    output = io.BytesIO()
    FigureCanvas(fig3).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure_3():
    fig3 = df.plot.scatter(x="StrDef (%)", y="TDDef (%)").get_figure()
    return fig3

@app.route('/download')
def downloadFile():
    path = "fighter.json"
    return send_file(path, as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)