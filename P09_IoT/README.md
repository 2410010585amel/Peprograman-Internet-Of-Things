# Praktikum IoT Pertemuan 9 - REST API, WebSocket & Custom Dashboard
**Nama:** Fadliatul Amaliyah  
**NPM:** 2410010585  
**Kelas:** 5C Reguler Banjarmasin  

## Fitur Pengembangan yang Diimplementasikan
1. **Endpoint `PUT /api/threshold`**: Mengatur batas maksimal suhu dan memicu peringatan otomatis ketika suhu melewati batas[cite: 32].
2. **Grafik Real-Time (Chart.js)**: Visualisasi grafik garis suhu dan kelembaban secara langsung di dashboard[cite: 32].
3. **Autentikasi Header `X-API-Key`**: Validasi kunci keamanan (`uniska-iot-2026`) pada endpoint API[cite: 32].
4. **WebSocket (`/ws/sensor`)**: Pembaruan data real-time dari Node-RED ke dashboard tanpa polling[cite: 32].
5. **Penyimpanan Riwayat Permanen (`localfilesystem`)**: Menyimpan data riwayat sensor secara permanen ke penyimpanan lokal[cite: 32].

## Cara Menjalankan
1. Jalankan broker Mosquitto: `mosquitto -c /opt/homebrew/etc/mosquitto/mosquitto.conf -v`[cite: 30]
2. Jalankan Node-RED: `node-red` lalu impor file `flows.json`[cite: 17, 30].
3. Jalankan simulator ESP32: `python3 simulasi_esp32.py`[cite: 30]
4. Buka `dashboard.html` di browser[cite: 31].
