from backAnalyst import mqtt_client

def start_mqtt():
    mqtt_client.client.loop_start()