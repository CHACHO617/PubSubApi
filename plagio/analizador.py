import pika
import json

def callback(ch, method, properties, body):
    mensaje = json.loads(body)
    estudiante = mensaje.get('estudiante')
    archivo = mensaje.get('archivo')
    print(f"[Plagio] Analizando archivo '{archivo}' enviado por {estudiante}...")

# Conexión con RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Asegura que el exchange exista
channel.exchange_declare(exchange='entregas.tareas', exchange_type='fanout')

# Cola nominal para este servicio
queue_name = 'plagio_queue'
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange='entregas.tareas', queue=queue_name)

print('[*] Servicio de Análisis de Plagio esperando mensajes...')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
