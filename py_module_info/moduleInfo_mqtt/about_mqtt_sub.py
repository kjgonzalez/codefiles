'''
basic intro to subscribing to a topic
'''

import time
import json
import paho.mqtt.client as pmq
#import argparse


_tmp = json.load(open('kconf.json','r'))
_host = _tmp['host']
_port = _tmp['port']
_user = _tmp['user']
_pass = _tmp['pass']
_topic = 'topic/test'

def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print("Connected successfully")
        client.subscribe(_topic)
    else:
        print(f"Connection failed: {reason_code}")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received on {msg.topic}: {msg.payload.decode()}")


if(__name__ == '__main__'):
    # Create MQTT client
    client = pmq.Client(pmq.CallbackAPIVersion.VERSION2)
    client.username_pw_set(_user, _pass)
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to broker
    client.connect(_host, _port, keepalive=60)

    client.subscribe(_topic)
    client.loop_start()
    time.sleep(10)
    client.loop_stop()

    client.disconnect()

    print("Disconnected")


# eof
