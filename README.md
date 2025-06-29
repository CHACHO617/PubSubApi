# 📨 Taller Pub/Sub con APIs y RabbitMQ – StreamEdu

Este proyecto forma parte del Progreso 3 de la materia Integración de Sistemas. Se implementa una arquitectura distribuida basada en el patrón **Publicador/Suscriptor (Pub/Sub)** utilizando **RabbitMQ** como middleware de mensajería y **Flask** para exponer APIs REST.

## 👥 Autores
- Enrique Merizalde
- Jossue Játiva
- Doménica Escobar
- Juan Aristizábal

---

## 🎯 Objetivo

Simular el procesamiento de tareas estudiantiles en la empresa ficticia **StreamEdu**, donde se desencadenan múltiples acciones en paralelo cada vez que un estudiante sube una tarea:

- ✅ Publicar mensajes al exchange
- ✅ Notificación al profesor
- ✅ Análisis de plagio 

Esto se realiza de forma desacoplada mediante un **exchange fanout de RabbitMQ**, que distribuye el mensaje a múltiples servicios consumidores.

---

## 📦 Arquitectura
![Arquitectura](https://i.ibb.co/ycy6gDMX/Frame-1171275863.png)

---

## 🛠 Tecnologías utilizadas
- Python 3.10+
- Flask
- Flasgger (Swagger UI)
- Pika (cliente RabbitMQ en Python)
- RabbitMQ (Docker)

---

## 🚀 Cómo ejecutar el sistema
### 1. Clonar el repositorio
<pre><code><pre><code>git clone https://github.com/CHACHO617/PubSubApi.git 
cd PubSubApi</code></pre></code></pre>

### 2. Levantar RabbitMQ con Docker
- Accede a RabbitMQ en: http://localhost:15672
- Usuario: guest | Contraseña: guest
![RabbitMQ](https://i.ibb.co/fVkPp98x/image-334.png))

### 3. Activar entorno virtual e instalar dependencias
Desde cada subcarpeta (publisher/, notificaciones/, plagio/), ejecuta:
<pre><code><pre><code>python -m venv .venv
.venv\Scripts\activate         # Windows</code></pre></code></pre>

### 4. Ejecutar servicios
🔵 Publisher (API para subir tareas)
<pre><code><pre><code> cd publisher
python app.py </code></pre></code></pre>
- Accede a Swagger UI en: http://localhost:5000/apidocs
- Endpoint disponible: POST /subir-tarea

🟠 Servicio de Análisis de Plagio
<pre><code><pre><code> cd plagio
python analizador.py </code></pre></code></pre>
- Muestra: [Plagio] Analizando archivo 'tarea.docx' enviado por Juan Pérez...

🟢 Servicio de Notificaciones
<pre><code><pre><code> cd notificaciones
python notificador.py </code></pre></code></pre>
- Muestra: [Notificación] Enviando correo al profesor del curso 'Integración de Sistemas' por entrega de Juan Pérez...

---

📥 Ejemplo de entrada JSON
<pre><code><pre><code> 
{
  "estudiante": "Juan Pérez",
  "curso": "Integración de Sistemas",
  "archivo": "tarea1.docx"
}
</code></pre></code></pre>

---

## 🧪 Validaciones aplicadas
- Campos requeridos: estudiante, curso, archivo
- Extensión de archivo válida: .docx, .txt, .csv, .pdf
- Se genera automáticamente fechaEnvio en el backend
- Si falla la validación, se devuelve un error 400 o 500 según el caso

---

## 📸 Evidencia

### 🔵 Publisher (API para subir tareas)
![P1](https://i.ibb.co/pvmpf3Xn/image-335.png)
![P2](https://i.ibb.co/N4ZJMNB/image-336.png)
![P3](https://i.ibb.co/C53Wr991/image-337.png)
![P4](https://i.ibb.co/pjHRpWB9/image-338.png)
![P5](https://i.ibb.co/5x54h9Jb/image-339.png)


### 🟠 Servicio de Análisis de Plagio
![S1](https://i.ibb.co/D0Qm4NY/image-340.png)
![S2](https://i.ibb.co/pj2yHVxf/image-341.png)
![S3](https://i.ibb.co/ynSKVJq7/image-342.png)


### 🟢 Servicio de Notificaciones
![S4](https://i.ibb.co/gMHy2wgz/image-343.png)
![S5](https://i.ibb.co/Wpn6nYSZ/image-344.png)
![S6](https://i.ibb.co/p6SK7Bjg/image-345.png)







