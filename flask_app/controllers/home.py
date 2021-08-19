
from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.dojo import Dojo

from flask_app.models.ninja import Ninja


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('index.html', dojos = dojos)

# displays

@app.route('/create/dojo', methods = ['POST'])
def create_dojo():
    Dojo.create_dojo (request.form)
    return redirect('/dojos')

@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_all()
    return render_template('ninja.html', dojos = dojos)

@app.route('/create/ninja', methods = ['POST'])
def create_ninja():
    Ninja.create_ninja (request.form)
    dojo_id = request.form['dojos_id']
    return redirect(f'/dojos/{dojo_id}')

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id':dojo_id
    }
    dojo = Dojo.show_dojo(data)
    return render_template('dojo.html', dojo = dojo)



