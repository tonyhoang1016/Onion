
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import time
import onionGpio
from datetime import datetime

# LED GPIO
led_pin = 1
pir_pin = 2
led_light_up_time = 5

led = onionGpio.OnionGpio(led_pin)
pir = onionGpio.OnionGpio(pir_pin)

led.setOutputDirection(0)
pir.setInputDirection()
direction = pir.getDirection()
print direction
#status = pir.setInputDirection()
#print status
#pir.setValue(0)
#print direction

while True:
#    value = pir.getValue().rstrip()
   value = pir.getValue()
#   print value
   if(value == "1"):
         print datetime.now(),
         print "motion_detected"
#        print 'GPIO%d input value: %d'%(pir, int(value))
         led.setValue(1)
         time.sleep(led_light_up_time)
#        pir.setValue(0)
         led.setValue(0)
