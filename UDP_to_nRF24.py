from RF24 import RF24
import time

# Define the pins connected to the nRF24L01 module
radio = RF24(22, 0)  # CE, CSN
radio.begin()
radio.setPALevel(RF24.PA_HIGH)
radio.openWritingPipe(0xF0F0F0F0E1LL)
radio.openReadingPipe(1, 0xF0F0F0F0D2LL)
radio.startListening()

while True:
    data, addr = sock.recvfrom(1024)  # Receive data from UDP stream
    print(f"Received {data} from {addr}")
    
    radio.stopListening()  # Stop listening to start transmitting
    radio.write(data)  # Send data over nRF24L01
    radio.startListening()  # Start listening again
    time.sleep(0.1)

