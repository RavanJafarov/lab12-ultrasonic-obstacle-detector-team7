# 🦇 Lab 12 - Ultrasonic Obstacle Detector
### Team 7 | EEC3612 Embedded Systems Lab (Week 13)

![RaspberryPi](https://img.shields.io/badge/Raspberry_Pi-3_Model_B-C51A4A)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![SR04](https://img.shields.io/badge/Sensor-SR04_Ultrasonic-blue)
![I2C_LCD](https://img.shields.io/badge/Display-I2C_LCD-orange)

---

## 👥 Team Members

| Name | Role |
|------|------|
| **Ravan Jafarov** | Team Leader, Hardware & Circuit Setup |
| Azar Aslanov | Hardware (SR04 & LCD wiring) |
| Riad Alizada | Code (Distance calculation & LCD logic) |
| Hasan Aliyev | Code (LEDs, Buzzer & Button mute logic) |

📅 **Date:** December 2025  
🎓 **Professor:** Kim Deokhwan  
🛠️ **LA:** Rasim Mahmudov

---

## 🎯 Objective

Build an **Obstacle Detection System** using Raspberry Pi 3 and an HC-SR04 Ultrasonic Sensor that:
- Measures real-time distance to obstacles.
- Displays distance and status on an **I2C LCD**.
- Indicates distance zones using **LEDs** (Green = Safe, Yellow = Caution, Red = Danger).
- Activates a **Buzzer** for close-range danger alerts.
- Includes a **Button** to temporarily mute the buzzer.

---

## 🔧 Components Used

| Component | Description |
|-----------|-------------|
| Raspberry Pi 3 Model B | Main controller |
| HC-SR04 Ultrasonic Sensor | Distance measurement |
| I2C LCD (PCF8574, 0x27) | 16x2 Real-time display |
| LEDs (Green, Yellow, Red) | Zone indicators |
| Active Buzzer | Audio alert for danger |
| Push Button | Mute buzzer |
| Breadboard & Jumper Wires | Connections |

---

## 📂 Project Structure

```
lab12-ultrasonic-obstacle-detector-team7/
├── README.md
├── obstacle_detector/
│   └── pyfile_ultrasonic.py
└── images/
    ├── circuit.jpg
    └── demo.jpg
```

---

## ⚙️ Raspberry Pi Configuration

### 1. Enable I2C
```bash
sudo raspi-config
```
Go to: **Interface Options** → **I2C** → **Enable** → **Finish** → **Reboot**

### 2. Create Virtual Environment & Install Libraries
```bash
mkdir obstacle_detector && cd obstacle_detector
python3 -m venv obstacle
source obstacle/bin/activate
pip install RPi.GPIO RPLCD smbus
```

---

## 🔌 Circuit Setup (Example GPIO Pins)

| Component | Raspberry Pi GPIO |
|-----------|-------------------|
| SR04 Trig | GPIO 23 |
| SR04 Echo | GPIO 24 (Use voltage divider if needed!) |
| Green LED | GPIO 17 |
| Yellow LED | GPIO 27 |
| Red LED | GPIO 22 |
| Buzzer | GPIO 25 |
| Button | GPIO 18 (INPUT_PULLUP) |
| LCD SDA | GPIO 2 (SDA) |
| LCD SCL | GPIO 3 (SCL) |

---

## 💻 Python Code

👉 See [`obstacle_detector/pyfile_ultrasonic.py`](obstacle_detector/pyfile_ultrasonic.py)

### How to Run on Raspberry Pi
```bash
source obstacle/bin/activate
python3 pyfile_ultrasonic.py
```

*Tip: You can also download it directly on RPi via terminal:*
```bash
wget https://rasimmax.com/fsm/pybook/pyfile_ultrasonic.py
```

---

## 📊 Results & Logic

✅ **Distance > 30 cm:** Green LED ON, LCD shows "SAFE".  
✅ **10 cm < Distance < 30 cm:** Yellow LED ON, LCD shows "CAUTION".  
✅ **Distance < 10 cm:** Red LED ON + Buzzer beeps, LCD shows "DANGER".  
✅ **Button Press:** Toggles Buzzer mute state without stopping the system.  

---

## 📝 Conclusion

This lab successfully integrated digital I/O (LEDs, Button, Buzzer), I2C communication (LCD), and precise timing measurements (SR04 Ultrasonic) to create a functional, real-time obstacle detection and alert system.

---

## 📄 License
Educational project for EEC3612 Embedded Systems course.
