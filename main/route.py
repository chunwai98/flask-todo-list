from flask import Flask, render_template, request, url_for, redirect,Blueprint

def register_route(app,):
    @app.route("/")
    def index():
        return render_template("index.html")