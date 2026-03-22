# ESP32 Environmental Monitoring System

## Overview
This project implements an IoT environmental monitoring system using an ESP32 microcontroller and Python. It acquires environmental data, transmits it to a computer, stores it, and visualizes it in real time.

## System Architecture
ESP32 → Serial Communication → Python → CSV Storage → Data Visualization

## Features
- Temperature, humidity, and light data acquisition
- Serial communication between ESP32 and PC
- Data logging with timestamps
- Data visualization using matplotlib

## Technologies
- ESP32 (Arduino IDE)
- Python
  - pyserial
  - pandas
  - matplotlib

## Project Structure
firmware/
esp32_sensor_node.ino

python/
serial_receiver.py
save_to_csv.py
plot_data.py

## How to Run

1. Upload the firmware to the ESP32

2. Run the data logging script:
   python save_to_csv.py

3. Generate plots:
   python plot_data.py

## Future Work
- Add WiFi-based communication
- Implement MQTT protocol
- Integrate database storage (SQLite or cloud)
- Add real-time dashboard (Streamlit)

## Future Work
- Add WiFi-based communication
- Implement MQTT protocol
- Integrate database storage (SQLite or cloud)
- Add real-time dashboard (Streamlit)
