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

- ✅ Notificación al profesor
- ✅ Análisis de plagio
- 🕓 (Extendible: generación de resumen, log audit trail)

Esto se realiza de forma desacoplada mediante un **exchange fanout de RabbitMQ**, que distribuye el mensaje a múltiples servicios consumidores.

---

## 📦 Arquitectura
![Arquitectura](https://ibb.co/Tx84PZnk)


