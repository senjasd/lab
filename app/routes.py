# -*- coding: utf-8 -*-
from flask import render_template
from app import app
@app.route('/index')
@app.route('/')
def index():

    user = {'username': "student" , 'use': 'calculator'}
    return render_template('index.html', title='Home', user=user)

@app.route('/stat')
def stat():
    user = {'username': "SEM" , 'use': 'game'}
    return '''<html>
    <head>
    <title> Home  - Microblog</title>
    </head>
    <body>
    <h1>Hello,''' + user["username"] + '''!</h1>
    <h2>come on , ''' + user['use'] + '''!</h2>
    </body>
    </html>'''
