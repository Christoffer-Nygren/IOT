# -*- coding: utf-8 -*-
from machine import Pin
import time
import pycom
from dht import DHT

pycom.heartbeat(False)

p_in = Pin('P16', mode=Pin.IN)
th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)

#Checks the sensors and returns data


def getSensorInfo():
   result = th.read()
   while not result.is_valid():
      time.sleep(.5)
      result = th.read()
   sensors = [result.temperature, result.humidity]
   return sensors

#Main function of the lopy


def run():
   while(1):
      value = p_in.value()
      t = time.time()
      if t % 600 == 0:  # Checks if 10 minutes has passed for updates
          sensors = getSensorInfo()
          pybytes.send_signal(2, sensors[0])
          pybytes.send_signal(3, sensors[1])
          print('Sent auto temp successfully!')
          time.sleep(1)
      if value == 0:  # Checks if button has been pressed
         sensors = getSensorInfo()
         result_string = "Temperature: {}°C and Humidity: {}%".format(
             sensors[0], sensors[1])
         pybytes.send_signal(1, result_string)
         print('Sending {}'.format(result_string))
         pycom.rgbled(0x220000)
         time.sleep(1)
      else:
         pycom.rgbled(0x000022)
         time.sleep(1)


run()
