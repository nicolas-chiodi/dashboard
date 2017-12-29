# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 15:25:06 2017

@author: nico
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ccc/')
def accueil():
    return render_template('Debug.html')


if __name__ == '__main__':
    app.run(debug=True)   
    
    
    