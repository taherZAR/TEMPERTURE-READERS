# 🌡️ TEMPERATURE-READERS

A MicroPython project on ESP32 that reads distance using an ultrasonic sensor and activates a buzzer and LED as an alarm. The alarm can be stopped using a push button.

---

## 📌 Features

- 🧠 Powered by **ESP32** and **MicroPython**
- 📏 Uses ** DHT22 ** to detect temperature
- 🚨 Activates **buzzer** and **LEDs** when temperature rises
- 🔁 normal reading after temperature decline

---

## 🛠️ Components Used

| Component        | Description                    |
|------------------|--------------------------------|
| ESP32            | Microcontroller                |
| DHT22            | Temperature sensor             |
| Passive Buzzer   | For audible alarm              |
| LED BAR GRAPH    | For visual alarm               |
| LCD 16X2(I2C)    | Temperature reader             |
| Resistors        | 220Ω (for LED), 10kΩ (for button pull-up) |

---

## 🧠 Logic Flow

1. Measure temperature using DHT22.
2. If temperature < 35°C:
   - Turn on LED and buzzer.

---

## ⚙️ Circuit Diagram

This project uses Wokwi for simulation.  
You can view and test the circuit live below:

▶️ **[Run Simulation on Wokwi](https://wokwi.com/projects/378890758264108033)**

---

## 🧾 Files Included

| File             | Purpose                                  |
|------------------|-------------------------------------------|
| `main.py`        | MicroPython code for ESP32               |
| `diagram.json`   | Wokwi circuit layout                     |
| `ssd1306.py`     | (Optional) OLED support if used          |

---

## 🧰 How to Run (Wokwi or Real ESP32)

### 🔁 Wokwi
1. Go to [wokwi.com](https://wokwi.com)
2. Click **"New Project" > "Import Project"**
3. Upload the files (`main.py`, `diagram.json`)
4. Click **Start Simulation**

### 🔌 Real ESP32 (optional)
1. Flash MicroPython firmware to your ESP32
2. Use Thonny or uPyCraft to upload `main.py`
3. Connect components as per diagram
4. Run the script

---

## 👤 Author

- 🔗 GitHub: [@taherZAR](https://github.com/taherZAR)
- 💡 Project: [TEMPERATURE-READERS](https://github.com/taherZAR/TEMPERTURE-READERS)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

