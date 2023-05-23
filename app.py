from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_pupil_position', methods=['POST'])
def get_pupil_position():
    # Obtener las coordenadas del cursor
    cursor_x = int(request.form['cursorX'])
    cursor_y = int(request.form['cursorY'])

    # Coordenadas del centro del gato
    gato_x = 0
    gato_y = 450

    # Calcular la diferencia entre las coordenadas del cursor y las del gato
    delta_x = cursor_x - gato_x
    delta_y = cursor_y - gato_y

    # Calcular las coordenadas de las pupilas del gato
    pupil_x = delta_x * 0.025
    pupil_y = delta_y * 0.04

    # Devolver las coordenadas de las pupilas
    return jsonify({'pupilX': pupil_x, 'pupilY': pupil_y})

if __name__ == '__main__':
    # Ejecutar la aplicación
    app.run()
