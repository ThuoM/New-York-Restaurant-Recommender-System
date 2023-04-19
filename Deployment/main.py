from flask import Flask,render_template, redirect, url_for,request,flash,get_flashed_messages,abort
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from wtforms import StringField, SubmitField, FileField
from wtforms.fields.simple import EmailField, PasswordField
from wtforms.validators import DataRequired, URL,Email
import sqlite3
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

#create connection
conn = sqlite3.connect('restaurant_recommender.db')
cursor = conn.cursor()

#read from db table
df = pd.read_sql("SELECT * FROM restaurants", conn)

def default_recommendations(df):
    random_samples = df.sample(n = 10, replace = True)
    return random_samples



@app.route('/')
def home():
    return render_template("index.html", recomms = default_recommendations(df))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)



