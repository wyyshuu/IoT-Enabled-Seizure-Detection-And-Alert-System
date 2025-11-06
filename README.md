# 🧠 IoT Enabled Seizure Detection and Alert System

## 🩺 About the Project
The **IoT Enabled Seizure Detection and Alert System** is a smart health monitoring device designed to detect seizure symptoms in real time and send instant alerts to caregivers.  
It continuously monitors vital body parameters such as **motion, heart rate, and body temperature**. When the system identifies abnormal readings that indicate a possible seizure, it immediately triggers a **buzzer alert** and sends **real-time notifications** through the **Blynk IoT platform**.

This project demonstrates how IoT can help in **early detection and emergency alerting** for patients with epilepsy or other neurological conditions.

---

## 🎯 Objective
To design and implement an IoT-based system that:
- Detects unusual body movements and abnormal vital signs.
- Sends instant alerts to caregivers via the Blynk app.
- Provides continuous health monitoring in real time.

---

## ⚙️ Hardware Components
| Component | Description |
|------------|-------------|
| **NodeMCU (ESP8266)** | Main microcontroller that processes sensor data and connects to Wi-Fi. |
| **Accelerometer Sensor (e.g., ADXL335)** | Detects sudden jerks or body movements. |
| **Pulse Sensor** | Measures heart rate in BPM. |
| **Temperature Sensor (e.g., LM35 / DHT11)** | Monitors body temperature. |
| **Buzzer** | Gives an audible alert when a seizure is detected. |
| **Power Supply** | USB or Li-ion battery. |

---

## 🧩 Software Requirements
- **Arduino IDE** – for coding and uploading the program.  
- **Blynk App** – for IoT dashboard and notifications.  
- **Cirkit Designer / Fritzing** – for creating the circuit connection diagram.  

---

## 🚀 Working Principle
1. Sensors continuously collect data such as motion, temperature, and heart rate.  
2. The microcontroller (NodeMCU) analyzes these readings in real time.  
3. If any parameter crosses a preset threshold (for example, rapid jerky motion + high pulse rate), the system detects it as a possible **seizure event**.  
4. It then:
   - Activates the **buzzer** for nearby people to assist.  
   - Sends **IoT alerts** through the **Blynk app** to caregivers or doctors.  
5. Caregivers can view live sensor readings and receive immediate notifications through their smartphones.

---

## 📱 Blynk Configuration
1. Create a new **Template** on [Blynk Cloud](https://blynk.cloud).  
2. Add the following **Datastreams**:
   - Temperature (V0)
   - Heart Rate (V1)
   - Motion / Vibration Status (V2)
3. Copy the **Auth Token** and paste it into your Arduino code.  
4. Run the project — the data will appear live on your dashboard.  
5. Set up **Event Notifications** in Blynk for automatic seizure alerts.

---

## 🖼️ Circuit Diagram
Include your circuit image here once ready:  
```
/circuit/design_diagram.png
```

---

## 📂 Repository Structure
```
IoT-Seizure-Detection/
├── code/
│   └── seizure_detection.ino
├── circuit/
│   └── design_diagram.png
├── docs/
│   └── project_report.pdf
└── README.md
```

---

## 🧠 Output
- Real-time monitoring of heart rate, motion, and temperature.  
- Automatic buzzer activation and IoT notification during abnormal readings.  
- Live dashboard visualization using the Blynk app.  

---

## 🌐 Applications
- Remote patient monitoring systems.  
- Smart healthcare and emergency alert systems.  
- Real-time epilepsy/seizure detection for home and hospital use.  

---

## 💡 Future Improvements
- Add **GPS** for location tracking during seizure alerts.  
- Integrate **Machine Learning** for predictive seizure detection.  
- Enable **Cloud storage** for long-term health data analysis.  

---

## 👩‍💻 Team
Developed by **Vaishnavi S** and team  
Department of **Electronics and Communication Engineering**  

---

## 📢 Conclusion
The **IoT Enabled Seizure Detection and Alert System** provides a cost-effective and reliable solution for real-time seizure detection.  
By combining IoT, sensors, and cloud connectivity, it enhances patient safety and ensures faster medical response in emergency situations.

---

⭐ *If you find this project helpful, don’t forget to star this repository!*  
