from flask import Flask, redirect
from flask import render_template
from flask import request
from dbservice import *

app = Flask(__name__)

@app.route("/go/<path:path>")
def go(path):
    links = read_from_db()
    return redirect(links[path])

@app.route("/register", methods=['GET', 'POST'])
def register():    
    if request.method == 'POST':
        go_name = request.form['go_name']
        go_link = request.form['go_link']
        
        try:
            links = read_from_db()
            links[go_name] = go_link
            message = "Success"
            write_to_db(links)
            return render_template('home.html', message=message)
        except Exception as error:
            print("An exception occurred:", error)
            message = "Error: " + error.message
            return render_template('home.html', message=message)
    else:
        return redirect("/")
    
@app.route("/")
def home():
        message = " "
        return render_template('home.html', message=message)

@app.route("/links")
def listLinks():
    links = read_from_db()
    return render_template('table.html', links=links)
