# -*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route('/')
def base():
    return render_template('base.html', title='Home')


@app.route('/index4')
def index4():
    user = {'username': "student", 'use': 'calculator'}
    names_fraz = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Василий'},
            'body': 'Привет!!'
        }
    ]
    return render_template('index4.html', title='Home', user=user, names_fraz=names_fraz)


@app.route('/stat')
def stat():
    user = {'username': "SEM" , 'use': 'game'}
    return '''<html>
    <head>
    <title> Home  - Shared Microblog</title>
    </head>
    <body>
    <h1>Hello,''' + user["username"] + '''!</h1>
    <h2>come on , ''' + user['use'] + '''!</h2>
    </body>
    </html>'''
