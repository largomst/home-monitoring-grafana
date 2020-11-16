import paho.mqtt.client as mqtt
import time
import random

print("run")


def on_connect(*argv, **kwargs):
    print("connected success")


client = mqtt.Client()
client.connect("broker.zkanghui.com", 1883)
client.on_connect = on_connect
while True:
    temperature = random.randint(20, 23)
    client.publish("livingroom/temperature", temperature)
    print(f"\r{temperature}", end="")
    time.sleep(0.5)
