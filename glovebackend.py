import socket
from time import sleep
import RPi.GPIO as GPIO
from mpu6050 import mpu6050
from pynput import keyboard

class GloveNetwork:
    def __init__(self):
        # Enable connection of single touch sensor for smart glove pressure input via GPIO connection to RPI
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)

        self.gyro = mpu6050(0x68)                                           # Connect to gyroscope module located on smart glove via RPI
        self.host = "Your IP"
        self.port = 8080

        self.running = True
    
    def establishCon(self):
        print("Initializing Glove Server Connection.")
        # Establish TCP connecting with receiving server while keeping socket stream reusable for infinite conectivity after main loop executes
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as gloveNode:
            gloveNode.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            gloveNode.bind((self.host, self.port))
            gloveNode.listen()
        
            gloveHostCon, hostAddr = gloveNode.accept()
            with gloveHostCon:
                gloveHostCon.sendall("[INIT_SEC_CON=?]".encode())               # Send connection request to the receiving device
                hostResponse = gloveHostCon.recv(1024).decode()
                if hostResponse == "[INIT_SEC_CON=T]":
                    print("Successfully Established Secure Connection With Host.")
                    while self.running:
                        # Send gyroscopic location of glove / hand only when sensor is pushed
                        if GPIO.input(21) == True:
                            pos = self.getAccelPos()
                            gloveHostCon.sendall(pos.encode())
                            sleep(0.1)

    def getAccelPos(self):
        accel_data = self.axis_mod.get_accel_data()
        x = str(accel_data['x'])
        y = str(accel_data['y'])
        z = str(accel_data['z'])
        pos = x + "|" + y + "|" + z                                             # Note that due to this format, the recieving host must appropriately index and convert the string to obtain raw positions.
            
        return pos
    
    def quit(self):
        self.running = False

glove = GloveNetwork()
glove.establishCon()

def terminate():
    glove.quit()
    
listener = keyboard.Listener(on_press = terminate)
listener.start()