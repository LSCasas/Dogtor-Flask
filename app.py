from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/veterinarios')
def veterinarios():
    return render_template('veterinarios.html')

@app.route('/dueños')
def dueños():
    return render_template('dueños.html')

@app.route('/citas')
def citas():
    return render_template('citas.html')

@app.route('/mascotas')
def mascotas():
    return render_template('mascotas.html')

@app.route('/procedimientos')
def procedimientos():
    return render_template('procedimientos.html')

if __name__ == '__main__':
    app.run(debug=True)
