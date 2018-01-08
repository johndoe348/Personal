# -*- coding: utf-8 -*-
"""
First, make sure flask is installed. Open the Anaconda prompt window and
enter the following command:

conda install flask
    Fetching package metadata ...........
    Solving package specifications: .
    
    Package plan for installation in environment C:\Users\chhall\AppData\Local\Continuum\Anaconda2:
    
    The following packages will be UPDATED:
    
        conda: 4.3.16-py27_0 --> 4.3.18-py27_0
        flask: 0.11.1-py27_0 --> 0.12.1-py27_0
    
    Proceed ([y]/n)? y
    
    flask-0.12.1-p 100% |###############################| Time: 0:00:00 396.25 kB/s
    conda-4.3.18-p 100% |###############################| Time: 0:00:00 604.68 kB/s

******************************************************************************

This is the hello.py script from the Flask documentation.
See http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
for details.

After starting the script in Spyder, open a web browser and enter the URL:
    http://127.0.0.1:5000/
The page should say, "Hello World!"
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
if __name__ == "__main__":
    app.run()
