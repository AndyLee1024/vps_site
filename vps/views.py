# coding=UTF-8
from vps import app
import MySQLdb
import requests
from flask import request, session, g, redirect, url_for, \
    abort, render_template, flash
import sys


def connect_db():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    conn = MySQLdb.connect(host=app.config['MYSQL_DATABASE_HOST'],
                           user=app.config['MYSQL_DATABASE_USER'],
                           passwd=app.config['MYSQL_DATABASE_PASSWORD'])
    conn.select_db(app.config['MYSQL_DATABASE_DB'])
    cursor = conn.cursor()
    cursor.execute("SET NAMES utf8");
    return cursor


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def index():
    g.db.execute('select * from goods')
    data = g.db.fetchone()
    return render_template('index.html', name=data)

@app.route('/packages')
def packages():
    data = {}
    data['title'] = 'fuck'
    return render_template('packages.html', name=data)

@app.route('/service')
def services():
    return render_template('service.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')