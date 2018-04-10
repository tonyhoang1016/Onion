import paho.mqtt.client as mqtt
import onionGpio
import time


broker="192.168.3.206"
#broker="192.168.1.14"


# instantiate a GPIO object
gpio0 = onionGpio.OnionGpio(1)
# set to output direction with zero (LOW) being the default value
gpio0.setOutputDirection(1)

# infinite loop - runs main program code continuously


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("home/led")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    if "ON" in msg.payload:
        gpio0.setValue(1)
    elif "OFF" in msg.payload:
        gpio0.setValue(0)
    else:
        gpio0.setValue(0)


    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# home
#client.connect("192.168.3.206", 1883, 60)

# lab
client.connect(broker, 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.

client.on_connect = on_connect
client.on_message = on_message

# home
#client.connect("192.168.3.206", 1883, 60)

# lab
client.connect(broker, 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
