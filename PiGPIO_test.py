import pigpio

pi = pigpio.pi()  # Connect to pigpiod

if not pi.connected:
    print("Failed to connect to pigpiod!")
    exit(1)

print("Successfully connected to pigpiod.")
