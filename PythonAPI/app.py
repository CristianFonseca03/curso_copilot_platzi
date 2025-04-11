from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/saludo', methods=['GET'])
def saludo():
    """
    Saludo API
    ---
    parameters:
      - name: cadenadeentrada
        in: query
        type: string
        required: true
        description: Cadena de entrada para el saludo
    responses:
      200:
        description: Respuesta exitosa con el mensaje de saludo
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: Hola Cristian desde la API de Python
    """
    cadenadeentrada = request.args.get('cadenadeentrada', '')
    respuesta = f"Hola {cadenadeentrada} desde la API de Python"
    return jsonify({'mensaje': respuesta})

if __name__ == '__main__':
    app.run(debug=True)