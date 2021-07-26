from network import WLAN
import machine
import main
from lib import key
wlan = WLAN(mode=WLAN.STA)

#Connects the lopy to the wifi
nets = wlan.scan()
for net in nets:
    if net.ssid == key.ssid:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, key.ssid_pass), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        print(wlan.ifconfig())
        break

machine.main(main)
