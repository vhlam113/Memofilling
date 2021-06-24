from flask import Flask, render_template, url_for ,redirect, session
from flask_wtf import FlaskForm
from wtforms import (StringField,)
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/report")
def report():
	return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)