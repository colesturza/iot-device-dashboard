import random
import time
import json
import os

import paho.mqtt.client as paho

from datetime import datetime, timezone
from paho import mqtt


def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)


def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client = paho.Client(client_id="deviceEmulator01", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set(
    os.environ.get("MOSQUITTO_USERNAME"), os.environ.get("MOSQUITTO_PASSWORD")
)
client.connect("10.0.0.109", 1883)

client.on_message = on_message
client.on_publish = on_publish

while True:

    message = json.dumps(
        {
            "timestamp": datetime.now(tz=timezone.utc).strftime(
                "%a %b %-d %H:%M:%S %Z %Y"
            ),
            "xAcc": random.randrange(25, 35, 1),
            "yAcc": random.randrange(25, 35, 1),
            "zAcc": random.randrange(25, 35, 1),
            "alphaAcc": random.randrange(25, 35, 1),
            "betaAcc": random.randrange(25, 35, 1),
            "omegaAcc": random.randrange(25, 35, 1),
        },
        indent=4,
        sort_keys=True,
        default=str,
    )

    client.publish("devices/deviceEmulator01/sensorData", message)
    time.sleep(1)
    client.loop()
