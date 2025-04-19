import paho.mqtt.client as mqtt
import json
import time
from decouple import config

# Configuración MQTT
MQTT_SERVER = "mosquitto"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_TOPIC = "products/update"

# Configurar cliente MQTT global
client = mqtt.Client()

# Callback de conexión
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado a MQTT broker")
    else:
        print(f"❌ Falló la conexión, código {rc}")

# Conectar al broker MQTT
def connect_mqtt():
    client.on_connect = on_connect
    client.connect(MQTT_SERVER, MQTT_PORT, MQTT_KEEPALIVE)
    client.loop_start()

# Función para publicar alerta de stock bajo
def publish_low_stock_alert(payload: dict, topic: str = MQTT_TOPIC):
    try:
        client.publish(topic, json.dumps(payload))
        print(f"📤 Publicando: {json.dumps(payload)}")
    except Exception as e:
        print(f"❌ Error publicando: {str(e)}")

# Conectar cuando inicie el servidor
connect_mqtt()