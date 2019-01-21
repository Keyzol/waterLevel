# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
print('-booting-')

import gc
import webrepl
import network

from machine import Pin, time_pulse_us, RTC, deepsleep, DEEPSLEEP
from time import sleep, sleep_us
from urequests import post

webrepl.start()
gc.collect()

# This portion connects to the network on boot
wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)       # activate the interface

try:
    wlan.connect('WIFI', 'password') # connect to an AP

except:
    sleep(60)
    rtc = RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=DEEPSLEEP)
    rtc.alarm(rtc.ALARM0, 540000)
    print('Network unavailable. Going to deepsleep ...')
    deepsleep()

    # put the device to sleep
    deepsleep()
ap = network.WLAN(network.AP_IF) # Disables the AP
ap.active(False)

# Assign Pins
trig = Pin(12, Pin.OUT)
echo = Pin(15, Pin.IN)

def distance():
    trig.off()
    sleep_us(5)
    trig.on()
    sleep_us(10)
    trig.off()

    pulse_time = time_pulse_us(echo, 1,20000)

    dist_m = (pulse_time / 2000000) * 343

    return dist_m

print('start distance measurement')

snt = False
tsr = '' # tank server response
cnt = 0

while (snt == False):
    sleep(3)
    try:
        rsp = post("http://xx.xx.xx.xx:PORT/tank", data=str(distance()))
        tsr = rsp.json()['status']
        print(tsr)
        rsp.close()
    except:
        print("= Trying again... =")
        cnt = cnt + 1
        pass
    if ( tsr == 'success'):
        snt = True
    elif ( cnt > 20):
        snt = True
