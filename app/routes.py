from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Usuario
from app.forms import MiFormulario 

# Crear un Blueprint para organizar las rutas
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def formulario():
    form = MiFormulario()  # Instancia del formulario

    if form.validate_on_submit():  # Verifica si el formulario es válido
        nombre = form.nombre.data
        email = form.email.data

        # Guardar en la base de datos
        nuevo_usuario = Usuario(nombre=nombre, email=email)
        db.session.add(nuevo_usuario)
        db.session.commit()

        return redirect(url_for('main.resultados'))

    return render_template('form.html', form=form)  # Pasar form a la plantilla

@main.route('/exito')
def exito():
    return render_template('success.html')

@main.route('/resultados')
def resultados():
    usuarios = Usuario.query.all()  # Obtener todos los usuarios de la BD
    return render_template('resultados.html', usuarios=usuarios)  # Pasar los datos
