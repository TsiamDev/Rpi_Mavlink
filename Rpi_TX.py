import pigpio
from NRF24 import NRF24
import time

pi = pigpio.pi()
if not pi.connected:
    print("Failed to connect to pigpiod!")
    exit(1)

pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]
radio = NRF24(pi, ce=22, csn=8, spi_channel=0)  # Adjust CE and CSN as needed
radio.begin()
radio.setPayloadSize(32)
radio.setChannel(76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])
radio.printDetails()

while True:
    message = list("Hello") + [0] * (32 - len("Hello"))
    radio.write(message)
    print("Sent:", message)
    time.sleep(1)
