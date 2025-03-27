from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

mongo_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?retryWrites=true&w=majority"

app = Flask(__name__)
app.config['MONGO_URI'] = mongo_uri
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')



################# CRUD para Citas #################

# Mostrar citas en la plantilla
@app.route('/citas')
def citas():
    citas = mongo.db.citas.find()
    lista_citas = []
    
    for cita in citas:
        cita['_id'] = str(cita['_id']) 
        lista_citas.append(cita)

    return render_template('citas.html', citas=lista_citas)

# Crear cita
@app.route("/citas/agregar", methods=['POST'])
def agregar_cita():

    fecha = request.form.get('fecha')
    hora = request.form.get('hora')
    id_mascota = request.form.get('id_mascota')
    id_veterinario = request.form.get('id_veterinario')
    id_procedimiento = request.form.get('id_procedimiento')

    print("Datos recibidos:", fecha, hora, id_mascota, id_veterinario, id_procedimiento)

    if fecha and hora and id_mascota and id_veterinario and id_procedimiento:
        mongo.db.citas.insert_one({
            "fecha": fecha,
            "hora": hora,
            "id_mascota": id_mascota,
            "id_veterinario": id_veterinario,
            "id_procedimiento": id_procedimiento,
        })
        print("Cita agregada correctamente")
    else:
        print("Error: Datos incompletos")

    return redirect(url_for('citas'))

# Obtener cita por ID
@app.route("/citas/obtenerPorId/<id>", methods=['GET'])
def obtener_cita_por_id(id):
    cita = mongo.db.citas.find_one({"_id": ObjectId(id)})
    if not cita:
        return redirect(url_for('citas'))
    cita['_id'] = str(cita['_id']) 
    return render_template('actualizar_cita.html', cita=cita)

# Actualizar cita
@app.route("/citas/actualizar/<id>", methods=['POST'])
def actualizar_cita(id):
    fecha = request.form.get('fecha')
    hora = request.form.get('hora')
    id_mascota = request.form.get('id_mascota')
    id_veterinario = request.form.get('id_veterinario')
    id_procedimiento = request.form.get('id_procedimiento')

    if fecha and hora and id_mascota and id_veterinario and id_procedimiento:
        mongo.db.citas.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "fecha": fecha,
                "hora": hora,
                "id_mascota": id_mascota,
                "id_veterinario": id_veterinario,
                "id_procedimiento": id_procedimiento
            }}
        )

    return redirect(url_for('citas'))

# Eliminar cita
@app.route("/citas/eliminar/<id>", methods=['POST'])
def eliminar_cita(id):
    mongo.db.citas.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('citas'))


################# CRUD para Veterinarios #################

# Mostrar veterinarios en la plantilla
@app.route('/veterinarios')
def veterinarios():
    veterinarios = mongo.db.veterinarios.find()
    lista_veterinarios = []
    
    for veterinario in veterinarios:
        veterinario['_id'] = str(veterinario['_id']) 
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
    veterinario['_id'] = str(veterinario['_id']) 
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
        dueño['_id'] = str(dueño['_id']) 
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
    dueño['_id'] = str(dueño['_id']) 
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






################# CRUD para Mascotas #################

# Mostrar mascotas en la plantilla
@app.route('/mascotas')
def mascotas():
    mascotas = mongo.db.mascotas.find()
    lista_mascotas = []
    
    for mascota in mascotas:
        mascota['_id'] = str(mascota['_id']) 
        lista_mascotas.append(mascota)

    return render_template('mascotas.html', mascotas=lista_mascotas)

# Crear mascota
@app.route("/mascotas/agregar", methods=['POST'])
def agregar_mascota():
    nombre = request.form.get('nombre')
    especie = request.form.get('especie')
    edad = request.form.get('edad')
    id_dueño = request.form.get('id_dueño')

    if nombre and especie and edad and id_dueño:
        mongo.db.mascotas.insert_one({
            "nombre": nombre,
            "especie": especie,
            "edad": edad,
            "id_dueño": ObjectId(id_dueño)  # Guardar como ObjectId
        })

    return redirect(url_for('mascotas'))

# Obtener mascota por ID
@app.route("/mascotas/obtenerPorId/<id>", methods=['GET'])
def obtener_mascota_por_id(id):
    mascota = mongo.db.mascotas.find_one({"_id": ObjectId(id)})
    if not mascota:
        return redirect(url_for('mascotas'))
    mascota['_id'] = str(mascota['_id']) 
    return render_template('actualizar_mascota.html', mascota=mascota)

# Actualizar mascota
@app.route("/mascotas/actualizar/<id>", methods=['POST'])
def actualizar_mascota(id):
    nombre = request.form.get('nombre')
    especie = request.form.get('especie')
    edad = request.form.get('edad')
    id_dueño = request.form.get('id_dueño')

    if nombre and especie and edad and id_dueño:
        mongo.db.mascotas.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "nombre": nombre,
                "especie": especie,
                "edad": edad,
                "id_dueño": ObjectId(id_dueño)  # Actualizar como ObjectId
            }}
        )

    return redirect(url_for('mascotas'))

# Eliminar mascota
@app.route("/mascotas/eliminar/<id>", methods=['POST'])
def eliminar_mascota(id):
    mongo.db.mascotas.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('mascotas'))




################# CRUD para Procedimientos #################

# Mostrar procedimientos en la plantilla
@app.route('/procedimientos')
def procedimientos():
    procedimientos = mongo.db.procedimientos.find()
    lista_procedimientos = []

    for procedimiento in procedimientos:
        procedimiento['_id'] = str(procedimiento['_id']) 
        lista_procedimientos.append(procedimiento)

    return render_template('procedimientos.html', procedimientos=lista_procedimientos)

# Crear procedimiento
@app.route("/procedimientos/agregar", methods=['POST'])
def agregar_procedimiento():
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    costo = request.form.get('costo')

    if nombre and descripcion and costo:
        mongo.db.procedimientos.insert_one({
            "nombre": nombre,
            "descripcion": descripcion,
            "costo": costo
        })

    return redirect(url_for('procedimientos'))

# Obtener procedimiento por ID
@app.route("/procedimientos/obtenerPorId/<id>", methods=['GET'])
def obtener_procedimiento_por_id(id):
    procedimiento = mongo.db.procedimientos.find_one({"_id": ObjectId(id)})
    if not procedimiento:
        return redirect(url_for('procedimientos'))
    procedimiento['_id'] = str(procedimiento['_id']) 
    return render_template('actualizar_procedimiento.html', procedimiento=procedimiento)

# Actualizar procedimiento
@app.route("/procedimientos/actualizar/<id>", methods=['POST'])
def actualizar_procedimiento(id):
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    costo = request.form.get('costo')

    if nombre and descripcion and costo:
        mongo.db.procedimientos.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"nombre": nombre, "descripcion": descripcion, "costo": costo}}
        )

    return redirect(url_for('procedimientos'))

# Eliminar procedimiento
@app.route("/procedimientos/eliminar/<id>", methods=['POST'])
def eliminar_procedimiento(id):
    mongo.db.procedimientos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('procedimientos'))


if __name__ == '__main__':
    app.run(debug=True)