import time
from pymavlink import mavutil

# Create a MAVLink node
mav = mavutil.mavlink_connection('udp:0.0.0.0:14550')

print("MAVLink emulator running...")

while True:
    # Simulate a heartbeat
    mav.mav.heartbeat_send(
        mavutil.mavlink.MAV_TYPE_QUADROTOR,
        mavutil.mavlink.MAV_AUTOPILOT_ARDUPILOTMEGA,
        0, 0, 0
    )
    print("Sent Heartbeat")
    time.sleep(1)
