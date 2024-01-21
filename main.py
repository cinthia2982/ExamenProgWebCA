from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_unitario = 9000
        total_sin_descuento = tarros * precio_unitario

        if 18 <= edad <= 30:
            descuento = 0.15 * total_sin_descuento
        elif edad > 30:
            descuento = 0.25 * total_sin_descuento
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento - descuento

        return render_template('resultado_ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        usuarios_registrados = {'juan': 'admin', 'pepe': 'user'}

        if usuario in usuarios_registrados and usuarios_registrados[usuario] == contraseña:
            mensaje = f'Bienvenido {usuario.capitalize()}'
        else:
            mensaje = 'Usuario o contraseña incorrecto'

        return render_template('resultado_ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
