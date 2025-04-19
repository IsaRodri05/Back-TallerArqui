from backAnalyst import mqtt_client

mqtt_started = False

def start_mqtt():
    global mqtt_started
    if not mqtt_started:
        mqtt_client.client.loop_start()
        mqtt_started = True
        print("🚀 MQTT iniciado")
    else:
        print("⏸️ MQTT ya estaba iniciado")