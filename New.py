# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 23:01:00 2017

@author: nico

"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/cont/")
def chart():
    return render_template('Reprise1.html')

     
if __name__ == "__main__":
    app.run(debug = True)


 