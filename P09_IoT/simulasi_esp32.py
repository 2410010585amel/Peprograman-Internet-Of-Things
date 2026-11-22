import paho.mqtt.client as mqtt
import json, time, random
from datetime import datetime

BROKER = "localhost"
TOPIC_SENSOR = "iot/sensor"
TOPIC_KONTROL = "iot/kontrol"

def on_connect(client, userdata, flags, rc, properties=None):
    print("Terhubung ke Broker MQTT!")
    client.subscribe(TOPIC_KONTROL)

def on_message(client, userdata, msg):
    print(f"← [PERINTAH AKTIVATOR] {msg.payload.decode()}", flush=True)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="ESP32-Simulator-Amell")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.loop_start()

print("ESP32 Simulator berjalan... Tekan Ctrl+C untuk berhenti.")
try:
    while True:
        data = {
            "suhu": round(random.uniform(25.0, 35.0), 1),
            "kelembaban": round(random.uniform(55.0, 85.0), 1),
            "timestamp": datetime.now().isoformat()
        }
        client.publish(TOPIC_SENSOR, json.dumps(data))
        print(f"→ Publish: {data}")
        time.sleep(3)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
