import paho.mqtt.client as mqtt
import time, random
client = mqtt.Client('hoa')
client.username_pw_set('mqttuser','mqttpassword')
client.connect('localhost',1883)
while True:
    value = random.randint(20,30)
    client.publish('home/lightroom/temperature', value)
    time.sleep(0.5)