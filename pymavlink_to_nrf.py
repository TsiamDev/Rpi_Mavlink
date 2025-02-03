import serial
import time
from pymavlink import mavutil
from RF24 import RF24

radio = RF24(22, 0)  # CE=GPIO22, CSN=SPI CE0
radio.begin()
radio.setChannel(76)
radio.setPALevel(RF24.PA_HIGH)
radio.setDataRate(RF24.DATA_RATE_250KBPS)
radio.openWritingPipe(b"1Node")
radio.stopListening()

# Setup MAVLink UART
pixhawk = serial.Serial('/dev/serial0', 57600, timeout=1)
mav = mavutil.mavlink_connection(pixhawk)

print("Forwarding MAVLink to NRF24L01...")

while True:
    msg = mav.recv_match(blocking=True)
    if msg:
        data = str(msg).encode()
        print("Sending:", data)
        radio.write(data[:32])  # NRF24 max payload = 32 bytes
        time.sleep(0.1)
