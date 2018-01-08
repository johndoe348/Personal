# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:12:31 2017

@author: KMCGI
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'