# Tugas Pertemuan 10: Dashboard Node-RED untuk Kontrol Relay dan Monitoring Suhu

Proyek mini Internet of Things (IoT) menggunakan protokol **MQTT (Mosquitto)** untuk menghubungkan simulasi perangkat sensor/aktuator berbasis **Python (`paho-mqtt`)** dengan antarmuka visual **Node-RED Dashboard**.

- **Nama:** Fadliatul Amaliyah
- **NIM:** 2410010585
- **Kelas:** 5C Reguler Banjarmasin
- **Mata Kuliah:** Pemrograman Internet of Things

---

## Arsitektur & Konfigurasi Topik MQTT

- **Broker:** Mosquitto Lokal (`localhost:1883`)
- **Interval Publish Sensor:** Setiap 3 detik

| Fungsi | Topik MQTT | Arah Komunikasi | Payload |
| :--- | :--- | :--- | :--- |
| **Monitoring Suhu (DHT22)** | `iot/2410010585/sensor/suhu` | Python → Node-RED (`ui_gauge`) | Nilai suhu dalam °C (Float) |
| **Kontrol Relay (GPIO 26)** | `iot/2410010585/aktuator/relay` | Node-RED (`ui_switch`) → Python | `"ON"` / `"OFF"` |
| **Kontrol PWM LED (GPIO 23)** | `iot/2410010585/aktuator/pwm` | Node-RED (`ui_slider`) → Python | Nilai integer `0` – `255` |

---

## Daftar File

- `tugas10_2410010585.py` — Skrip Python client MQTT yang mem-publish data suhu simulasi DHT22 setiap 3 detik serta men-subscribe perintah kendali Relay (GPIO 26) dan kecerahan LED PWM (GPIO 23).
- `flow_p10_2410010585.json` — File hasil ekspor flow Node-RED berisi node `mqtt in`, `mqtt out`, `function`, `ui_gauge`, `ui_switch`, dan `ui_slider`.
- `screenshot_dashboard.png` — Tangkapan layar tampilan Node-RED Dashboard yang sedang berjalan.
- `demo_kontrol_p10.mov` — Rekaman video singkat (maks. 60 detik) demonstrasi kontrol Relay dan PWM dari dashboard ke perangkat.
