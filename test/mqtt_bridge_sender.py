import paho.mqtt.client as mqtt
import threading
import time
URL = "broker.zkanghui.com"
PORT = 1883

count = 0

lock = threading.Lock()

def task():
    global count

    client = mqtt.Client()
    client.connect(URL, PORT)

    while True:
        with lock:
            count += 1
            print(f"\r{count}", end="")
            client.publish('thread', count)
        time.sleep(0.5)

for i in range(1000):
    t = threading.Thread(target=task)
    t.start()