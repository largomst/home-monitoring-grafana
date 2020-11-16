import paho.mqtt.client as mqtt

URL = "broker.zkanghui.com"
PORT = 1883
count = 0

def on_connect(*argv):
    print('connected')


def on_message(client, userdata, msg):
    global count
    if msg.topic == 'thread':
        count += 1
        print(f"\r{count}", end="")

client = mqtt.Client()
client.connect(URL, PORT)


client.on_connect = on_connect
client.on_message = on_message
client.subscribe("+/#")

client.loop_forever()