from djitellopy import tello
from time import sleep

kair = tello.Tello()
kair.connect()
print(kair.get_battery())

kair.takeoff()
kair.move_up(500)
kair.send_rc_control(0, 50, 0, 0)
sleep(20)
kair.send_rc_control(0, 50, 0, 0)
sleep(20)
kair.send_rc_control(0, 0, 0, 0)
kair.land()
