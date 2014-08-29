#!/usr/bin/python
# coding=UTF-8
__author__ = 'andylee'

from flask import Flask

# configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

MYSQL_DATABASE_HOST = '127.0.0.1'
MYSQL_DATABASE_PORT	=  '3306'
MYSQL_DATABASE_USER	=  'root'
MYSQL_DATABASE_PASSWORD	= 'root'
MYSQL_DATABASE_DB = 'ychebao'
MYSQL_DATABASE_CHARSET = 'utf-8'


app = Flask(__name__)
app.config.from_object(__name__)

import vps.views
