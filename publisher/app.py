from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
import pika, json
from datetime import datetime

app = Flask(__name__)
swagger = Swagger(app)

EXTENSIONES_VALIDAS = {'.docx', '.txt', '.csv', '.pdf'}

def extension_valida(nombre_archivo):
    return any(nombre_archivo.endswith(ext) for ext in EXTENSIONES_VALIDAS)

@app.route('/subir-tarea', methods=['POST'])
@swag_from({
    'tags': ['Tareas'],
    'consumes': ['application/json'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'estudiante': {'type': 'string', 'example': 'Enrique Merizalde'},
                    'curso': {'type': 'string', 'example': 'Integración de Sistemas'},
                    'archivo': {'type': 'string', 'example': 'tarea2.docx'}
                },
                'required': ['estudiante', 'curso', 'archivo']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Tarea enviada correctamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'mensaje': {'type': 'string'},
                    'datos': {'type': 'object'}
                }
            }
        },
        400: {
            'description': 'Error de validación'
        },
        500: {
            'description': 'Error interno en RabbitMQ'
        }
    }
})
def subir_tarea():
    data = request.get_json()

    campos_requeridos = {'estudiante', 'curso', 'archivo'}
    if not all(campo in data for campo in campos_requeridos):
        return jsonify({"error": "Faltan campos requeridos: estudiante, curso, archivo"}), 400

    if not extension_valida(data['archivo']):
        return jsonify({
            "error": f"Extensión no permitida. Solo se aceptan: {', '.join(EXTENSIONES_VALIDAS)}"
        }), 400

    data['fechaEnvio'] = datetime.now().isoformat()

    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='entregas.tareas', exchange_type='fanout')
        channel.basic_publish(exchange='entregas.tareas', routing_key='', body=json.dumps(data))
        connection.close()
    except Exception as e:
        return jsonify({"error": "Error al conectar con RabbitMQ", "detalle": str(e)}), 500

    return jsonify({"mensaje": "Tarea enviada correctamente", "datos": data}), 200

if __name__ == '__main__':
    app.run(port=5000)
