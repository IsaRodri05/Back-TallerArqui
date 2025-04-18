import paho.mqtt.client as mqtt
import json
import random
import time
from datetime import datetime
from decouple import config

# Configuración MQTT
MQTT_SERVER = "mosquitto"  # Nombre del servicio en docker-compose
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_TOPIC = "products/update"

# Función para generar datos "moqueados"
def generate_mock_data():
    products = ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E"]
    product_name = random.choice(products)
    date = datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H:%M")
    quantity = random.randint(1, 10)
    
    return {
        "nombre": product_name,
        "fecha": date,
        "hora": time_str,
        "cantidad": quantity
    }

# Callback de conexión
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado a MQTT broker")
    else:
        print(f"❌ Falló la conexión, código {rc}")

# Configurar cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.connect(config('MQTT_SERVER'), int(config('MQTT_PORT')), int(config('MQTT_KEEPALIVE')))

client.loop_start()

# Publicar datos "moqueados" cada 5 segundos
while True:
    mock_data = generate_mock_data()
    payload = json.dumps(mock_data)
    client.publish(config('MQTT_TOPIC'), payload)
    print(f"📤 Publicando: {payload}")
    time.sleep(5)  # Espera de 5 segundos antes de enviar el siguiente mensaje
