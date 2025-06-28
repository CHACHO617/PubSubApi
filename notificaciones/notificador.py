import pika
import json

def callback(ch, method, properties, body):
    mensaje = json.loads(body)
    estudiante = mensaje.get('estudiante')
    curso = mensaje.get('curso')
    print(f"[Notificación] Enviando correo al profesor del curso '{curso}' por entrega de {estudiante}...")

# Conexión con RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Asegura que el exchange exista
channel.exchange_declare(exchange='entregas.tareas', exchange_type='fanout')

# Cola anónima exclusiva (autogenerada)
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='entregas.tareas', queue=queue_name)

print('[*] Servicio de Notificación esperando mensajes...')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
