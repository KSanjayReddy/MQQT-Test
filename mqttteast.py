import paho.mqtt.client as mqtt
import time


c1=mqtt.Client()
print("test")
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
########################################


c1.connect("iot.eclipse.org") #connect to broker
c1.on_message=on_message

c1.loop_start()
c1.subscribe("winchat")
while True:
    msg=raw_input("Message: ")
    if len(msg)>0:
        print(msg)
        c1.publish("winchat"," "+msg)


time.sleep(4)
print("finish")
