from machine import Pin
from libs.uln2003 import Uln2003


motor = Uln2003(pin1=Pin(19), pin2=Pin(18), pin3=Pin(5), pin4=Pin(17), delay=1, mode='HALF_STEP')

motor.angle(180 , 1)
