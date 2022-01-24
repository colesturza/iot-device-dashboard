# simulator device 1 for mqtt message publishing
import random
import paho.mqtt.client as paho
import time
from datetime import datetime, timezone
import json

# hostname
broker = "localhost"

# port
port = 1883


def on_publish(client, userdata, result):
    print("Device 1 : Data published.")
    pass


client = paho.Client("device1")
client.on_publish = on_publish
client.connect(broker, port)

for i in range(100_000):
    # telemetry to send
    message = json.dumps(
        {
            "timestamp": datetime.now(tz=timezone.utc).strftime(
                "%a %b %-d %H:%M:%S %Z %Y"
            ),
            "metadata": {
                "device_id": "device01",
                "sensor_id": "sensor01",
                "measurement": "windspeed",
                "units": "mph",
            },
            "value": random.randrange(25, 35, 1),
        },
        indent=4,
        sort_keys=True,
        default=str,
    )
    time.sleep(1)

    # publish message
    ret = client.publish("sensors/data", message)

client.disconnect(broker, port)
print("Stopped...")
