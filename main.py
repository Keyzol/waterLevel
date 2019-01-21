# This fileruns after boot.py
print("--running Main.py--")

from machine import RTC, deepsleep, DEEPSLEEP
from time import sleep

def dsleep(msec):
    # configure RTC.ALARM0 to be able to wake the device
    rtc = RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=DEEPSLEEP)

    # set RTC.ALARM0 to fire after some milliseconds
    rtc.alarm(rtc.ALARM0, msec)

    # put the device to sleep
    deepsleep()

# Pause 1 minutes then sleep for 15 minutes 
sleep(60)
print('Going to deepSleep')
dsleep(840000) #14 minutes sleep