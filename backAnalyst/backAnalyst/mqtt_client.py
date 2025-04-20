import paho.mqtt.client as mqtt
import json
from decouple import config

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado a MQTT broker")
        client.subscribe(config('MQTT_TOPIC'))
    else:
        print(f"❌ Falló la conexión, código {rc}")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print("📥 Mensaje recibido:")
        print(f"📦 Producto: {payload['nombre']}")
        print(f"📅 Fecha: {payload['fecha']}")
        print(f"⏰ Hora: {payload['hora']}")
        print(f"🔢 Cantidad: {payload['cantidad']}")
    except Exception as e:
        print(f"❗ Error procesando el mensaje: {e}")

def start_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(
        config('MQTT_SERVER'),
        int(config('MQTT_PORT')),
        int(config('MQTT_KEEPALIVE'))
    )
    client.loop_forever()