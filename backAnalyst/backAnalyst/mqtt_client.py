import paho.mqtt.client as mqtt

MQTT_SERVER = "broker.emqx.io"
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("test/topic")
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT, MQTT_KEEPALIVE)


