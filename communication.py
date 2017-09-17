import paho.mqtt.client as mqtt
import time
import serial

c1=mqtt.Client()
print("test")
#ser = serial.Serial('/dev/ttyMCC', 9600)
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    #ser.write(str(message.payload.decode("utf-8")))

    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
########################################
#ser = serial.Serial('/dev/ttyMCC', 9600)
#print("message retain flag=",message.retain)

c1.connect("iot.eclipse.org") #connect to broker
c1.on_message=on_message

c1.loop_start()
c1.subscribe("winchat")
while True:
    msg=raw_input("Message: ")
    if len(msg)>0:
        print(msg)
        c1.publish("winchat"," "+msg)

   # sermsg=ser.readline()
    #print("serial:")
    #print(sermsg)


time.sleep(4)
print("finish")
