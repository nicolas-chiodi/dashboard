# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 23:01:00 2017

@author: nico

"""

from flask import Flask, render_template
import datetime as dt

dt.date.today()
Year = dt.date.today().year
Month = dt.date.today().month
Day = dt.date.today().day

app = Flask(__name__)
@app.route("/cont/")
def chart():
    dt.date.today()
    Year = dt.date.today().year
    Month = dt.date.today().month
    Day = dt.date.today().day
    T= [Year, Month, Day]
    return render_template('Dashboard1.html', Liste = T, HYear =Year,
                           HMonth = Month, HDay = Day)
 
 
     
if __name__ == "__main__":
    app.run(debug = True)

 
 
 