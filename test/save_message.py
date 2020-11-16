import paho.mqtt.client as mqtt
import csv
import time, random

f = open('./carMessage.txt','a')

def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(payload)
    f.write(payload + '\n')
    f.flush()

client = mqtt.Client('hoa')
client.username_pw_set('mqttuser','mqttpassword')
client.connect('broker.zkanghui.com',1883)
client.on_message = on_message
client.subscribe('carMessage')
client.loop_forever()
