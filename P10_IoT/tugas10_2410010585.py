import time
import random
import threading
import paho.mqtt.client as mqtt

# ================= KONFIGURASI NIM =================
NIM = "2410010585"
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_CLIENT_ID = f"PythonDevice-{NIM}"

# Topik sesuai instruksi tugas
TOPIC_SUHU = f"iot/{NIM}/sensor/suhu"
TOPIC_RELAY = f"iot/{NIM}/aktuator/relay"
TOPIC_PWM = f"iot/{NIM}/aktuator/pwm"

INTERVAL_PUBLISH = 3  # Wajib 3 detik sesuai instruksi tugas
relay_state = "OFF"
pwm_value = 0

# ================= CALLBACK MQTT =================
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[MQTT] Terhubung ke broker sebagai {MQTT_CLIENT_ID}")
        client.subscribe([(TOPIC_RELAY, 0), (TOPIC_PWM, 0)])
        print(f"[MQTT] Subscribe ke: {TOPIC_RELAY} & {TOPIC_PWM}")
    else:
        print(f"[MQTT] Gagal terhubung, kode: {rc}")

def on_message(client, userdata, msg):
    global relay_state, pwm_value
    payload = msg.payload.decode("utf-8").strip()
    print(f"[MQTT] Pesan masuk [{msg.topic}]: {payload}")

    # 1. Kontrol Relay pada GPIO 26
    if msg.topic == TOPIC_RELAY:
        if payload in ("ON", "1"):
            relay_state = "ON"
            print("[AKTUATOR - GPIO 26] RELAY MENYALA (ON)")
        elif payload in ("OFF", "0"):
            relay_state = "OFF"
            print("[AKTUATOR - GPIO 26] RELAY MATI (OFF)")
        else:
            print(f"[AKTUATOR - GPIO 26] Perintah relay tidak valid: {payload}")

    # 2. Kontrol Kecerahan LED PWM (0-255) pada GPIO 23
    elif msg.topic == TOPIC_PWM:
        try:
            nilai = int(float(payload))
            if 0 <= nilai <= 255:
                pwm_value = nilai
                persen = round((pwm_value / 255) * 100)
                print(f"[AKTUATOR - GPIO 23] Kecerahan LED PWM diatur ke: {pwm_value}/255 ({persen}%)")
            else:
                print(f"[AKTUATOR - GPIO 23] Nilai PWM di luar batas (0-255): {nilai}")
        except ValueError:
            print(f"[AKTUATOR - GPIO 23] Format nilai PWM tidak valid: {payload}")

def on_disconnect(client, userdata, rc):
    print(f"[MQTT] Terputus (kode: {rc}). Mencoba reconnect...")

# ================= SIMULASI SENSOR DHT22 =================
def baca_suhu_dht22():
    base = 27.5
    noise = random.uniform(-1.5, 1.5)
    return round(base + noise, 2)

# ================= THREAD PUBLISH SUHU (3 DETIK) =================
def publish_loop(client):
    while True:
        suhu = baca_suhu_dht22()
        client.publish(TOPIC_SUHU, str(suhu), qos=0)
        print(f"[SENSOR DHT22] Publish suhu: {TOPIC_SUHU} -> {suhu} °C")
        time.sleep(INTERVAL_PUBLISH)

# ================= PROGRAM UTAMA =================
def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id=MQTT_CLIENT_ID, protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    print(f"[MQTT] Menghubungkan ke {MQTT_BROKER}:{MQTT_PORT}...")
    client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
    client.loop_start()
    time.sleep(1)

    publisher = threading.Thread(target=publish_loop, args=(client,), daemon=True)
    publisher.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[MAIN] Program dihentikan.")
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()