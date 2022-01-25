#!/usr/bin/env bash

# Source: https://notes.lebster.me/posts/fast-way-to-run-a-secured-mosquitto-mqtt-broker-in-the-docker/

set -e

if ( [ -z "${MOSQUITTO_USERNAME}" ] || [ -z "${MOSQUITTO_PASSWORD}" ] ); then
  echo "MOSQUITTO_USERNAME or MOSQUITTO_PASSWORD not defined"
  exit 1
fi

# create mosquitto passwordfile
touch /mosquitto/config/mosquitto.passwd
mosquitto_passwd -b /mosquitto/config/mosquitto.passwd $MOSQUITTO_USERNAME $MOSQUITTO_PASSWORD

exec "$@"