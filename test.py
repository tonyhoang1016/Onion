import time
import onionGpio

gpioNum = 2
ledgpio = 1
gpioObj = onionGpio.OnionGpio(gpioNum)
ledObj = onionGpio.OnionGpio(ledgpio)

# set to input
status  = gpioObj.setInputDirection()

# set output
ledObj.setOutputDirection(0)

# read and print the value once a second
loop = 1
while loop == 1:
        value = gpioObj.getValue()
        print('GPIO%d input value: %d'%(gpioNum, int(value)))
        if int(value) == 1:
                ledObj.setValue(1)
                time.sleep(5)
        else:
                ledObj.setValue(0)
#       ledStatus = 1
        time.sleep(1)
#        ledStatus = 0

