from crypt import methods
import imp
from pydoc import render_doc
from unicodedata import name

from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.models_dojo import Dojo
from flask_app.models.models_ninja import Ninjas


@app.route('/')
def index():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos=dojos)


@app.route('/new_dojo', methods=['POST'])
def new_dojo():
    Dojo.save(request.form)
    return redirect('/')


@app.route('/add_ninja')
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos=dojos)


@app.route('/new_ninja', methods=['POST'])
def add_new_ninja():
    Ninjas.save(request.form)
    return redirect('/')


@app.route('/dojo_show/<int:dojo_id>')
def dojo_show(dojo_id):
    data = {
        "id": dojo_id
    }
    return render_template('dojo_show.html', dojo=Ninjas.get_ninjas_from_dojo(data))


@app.route('/create_ninja', methods=['POST'])
def create_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos=dojos)


# @app.route('/new_ninja', methods=['POST'])
# def new_ninja():
#     return render_template('/')
