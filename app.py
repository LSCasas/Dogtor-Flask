from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/Dogtor"
mongo = PyMongo(app)

@app.route('/veterinarios', methods=['GET', 'POST'])
def veterinarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']

        if nombre and especialidad and telefono:
            mongo.db.Veterinario.insert_one({
                "nombre": nombre,
                "especialidad": especialidad,
                "telefono": telefono
            })
        return redirect(url_for('veterinarios'))

    veterinarios = list(mongo.db.Veterinario.find())
    return render_template('veterinarios.html', veterinarios=veterinarios)

@app.route('/veterinarios/eliminar/<id>', methods=['POST'])
def eliminar_veterinario(id):
    mongo.db.Veterinario.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('veterinarios'))

@app.route('/veterinarios/editar/<id>', methods=['GET', 'POST'])
def editar_veterinario(id):
    veterinario = mongo.db.Veterinario.find_one({"_id": ObjectId(id)})

    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']

        if nombre and especialidad and telefono:
            mongo.db.Veterinario.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"nombre": nombre, "especialidad": especialidad, "telefono": telefono}}
            )
        return redirect(url_for('veterinarios'))

    return render_template('editar_veterinario.html', veterinario=veterinario)

if __name__ == '__main__':
    app.run(debug=True)
