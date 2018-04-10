import subprocess
import time
import paho.mqtt.publish as publish

broker="192.168.29.227"
#broker="192.168.1.10"

while True:

    process = subprocess.Popen(['dht-sensor', '0', 'DHT11', 'json'],
    stdout=subprocess.PIPE)

    stdout = process.communicate()[0]
    print stdout

#    exec(open('dht-sensor 0 DHT11 json'.read())

    publish.single("home/sensor", stdout, hostname=broker, port=1883)
    time.sleep(10)
