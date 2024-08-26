from flask import app, render_template

def get_redoc():
    return render_template("redoc.html")