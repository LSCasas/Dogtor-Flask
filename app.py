from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/Dogtor"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

################# CRUD para Veterinarios #################

# Mostrar veterinarios en la plantilla
@app.route('/veterinarios')
def veterinarios():
    veterinarios = mongo.db.veterinarios.find()
    lista_veterinarios = []
    
    for veterinario in veterinarios:
        veterinario['_id'] = str(veterinario['_id'])  # Convertir ObjectId a string
        lista_veterinarios.append(veterinario)

    return render_template('veterinarios.html', veterinarios=lista_veterinarios)

# Crear veterinario
@app.route("/veterinarios/agregar", methods=['POST'])
def agregar_veterinario():
    nombre = request.form.get('nombre')
    especialidad = request.form.get('especialidad')
    telefono = request.form.get('telefono')

    if nombre and especialidad and telefono:
        mongo.db.veterinarios.insert_one({
            "nombre": nombre,
            "especialidad": especialidad,
            "telefono": telefono
        })

    return redirect(url_for('veterinarios'))


@app.route("/veterinarios/obtenerPorId/<id>", methods=['GET'])
def obtenerPorId(id):
    veterinario = mongo.db.veterinarios.find_one({"_id": ObjectId(id)})
    if not veterinario:
        return redirect(url_for('veterinarios'))
    veterinario['_id'] = str(veterinario['_id'])  # Convertir ObjectId a string
    return render_template('actualizar_veterinario.html', veterinario=veterinario)

# Actualizar veterinario
@app.route("/veterinarios/actualizar/<id>", methods=['POST'])
def actualizar_veterinario(id):
    nombre = request.form.get('nombre')
    especialidad = request.form.get('especialidad')
    telefono = request.form.get('telefono')

    if nombre and especialidad and telefono:
        mongo.db.veterinarios.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"nombre": nombre, "especialidad": especialidad, "telefono": telefono}}
        )

    return redirect(url_for('veterinarios'))

# Eliminar veterinario
@app.route("/veterinarios/eliminar/<id>", methods=['POST'])
def eliminar_veterinario(id):
    mongo.db.veterinarios.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('veterinarios'))


################# CRUD para Dueños #################

# Mostrar dueños en la plantilla
@app.route('/dueños')
def dueños():
    dueños = mongo.db.dueños.find()
    lista_dueños = []
    
    for dueño in dueños:
        dueño['_id'] = str(dueño['_id'])  # Convertir ObjectId a string
        lista_dueños.append(dueño)

    return render_template('dueños.html', dueños=lista_dueños)

# Crear dueño
@app.route("/dueños/agregar", methods=['POST'])
def agregar_dueño():
    nombre = request.form.get('nombre')
    direccion = request.form.get('direccion')
    telefono = request.form.get('telefono')

    if nombre and direccion and telefono:
        mongo.db.dueños.insert_one({
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono
        })

    return redirect(url_for('dueños'))

# Obtener dueño por ID
@app.route("/dueños/obtenerPorId/<id>", methods=['GET'])
def obtener_dueño_por_id(id):
    dueño = mongo.db.dueños.find_one({"_id": ObjectId(id)})
    if not dueño:
        return redirect(url_for('dueños'))
    dueño['_id'] = str(dueño['_id'])  # Convertir ObjectId a string
    return render_template('actualizar_dueño.html', dueño=dueño)

# Actualizar dueño
@app.route("/dueños/actualizar/<id>", methods=['POST'])
def actualizar_dueño(id):
    nombre = request.form.get('nombre')
    direccion = request.form.get('direccion')
    telefono = request.form.get('telefono')

    if nombre and direccion and telefono:
        mongo.db.dueños.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"nombre": nombre, "direccion": direccion, "telefono": telefono}}
        )

    return redirect(url_for('dueños'))

# Eliminar dueño
@app.route("/dueños/eliminar/<id>", methods=['POST'])
def eliminar_dueño(id):
    mongo.db.dueños.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('dueños'))


if __name__ == '__main__':
    app.run(debug=True)