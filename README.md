# TCP-Controlled-Smart-Glove-Back-End-

## Overview
This project includes all the tools required to create a TCP connected smart glove using a Raspberry Pi, the mpu6050 gyroscopic sensor, a capacative touch sensor, and GPIO to generate signals to a host device to obtain the exact location of a users hand when a sensor is triggered.

## Usages
Potential use cases for this project include for VR gaming, or 3D interfaces where knowledge of hand positioning under certain configurations is required.

## Limitations
Though this project specifies the glove-level connections, establishing a host connection to a computer is left as a task for the user. The architecture laid out by this project is more than sufficient to create custom architecture that can be used to obtain glove gyroscopic signals when desired.

## Installation
1. Clone Repository
```
git clone https://github.com/mtgith/TCP-Controlled-Smart-Glove-Back-End-.git
cd TCP-Controlled-Smart-Glove-Back-End
```
2. Create venv on Raspberry Pi
```
conda create -n tcpglove python=3.8
```
3. Install Requirements
```
pip install -r requirements.txt
```
4. Connect GPIO Pins for capacitive sensor and mpu6050 module using specified links below:
```
https://learn.adafruit.com/capacitive-touch-sensors-on-the-raspberry-pi/wiring
https://www.electronicwings.com/raspberry-pi/mpu6050-accelerometergyroscope-interfacing-with-raspberry-pi
```
5. Initialize server on host PC.
6. Execute glovebackend.py.

## Spider-Man Web Shooters Mini-Program Example (Made with PyQt)
<img width="423" height="557" alt="Screenshot 2026-07-12 at 10 46 30 PM" src="https://github.com/user-attachments/assets/c65e8e47-3e9d-40ca-a891-1f04d3178bfb" />

