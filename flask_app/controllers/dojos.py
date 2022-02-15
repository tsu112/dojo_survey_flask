from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    Dojo.create(request.form)
    return redirect('/success')


@app.route('/success')
def success():
    return render_template('success.html', dojo=Dojo.last_survey())
