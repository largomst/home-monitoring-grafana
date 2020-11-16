from socket import timeout
from threading import Thread
import  paho.mqtt.client as mqtt
import time

url = "broker.zkanghui.com"
port = 1883


def pulish(index):
    client = mqtt.Client(f"python-client-{index}")
    client.connect(url, port,)
    while True:
        m = f"come from {index}"
        print(m)
        client.publish(f'thread/{index}', m)
        time.sleep(0.5)


for i in range(10000):
    thread = Thread(
        target=pulish,
        args=(i,),
    )
    thread.start()

