# iot-device-dashboard

This project utilizes a number of open source technologies to recored and display data collected by IoT devices. 
The primary tech stack includes Kubernetes, InfluxDB, Telegraf, Eclipse Misquitto, and Grafana (Maybe). The `emulate`
directory is provided to simulate traffic.

## How to deploy?

### Docker Compose

You will first need to install docker-compose.

Create a file called `.env` in the root directory of this project. It needs to contain the following environmental variables.

```
DOCKER_INFLUXDB_INIT_PASSWORD=pass
DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=token
MOSQUITTO_USERNAME=user
MOSQUITTO_PASSWORD=pass
```

Replace the above with the approaprate credentials. Run the folowing command from the root directory of this project.

```bash
docker-compose up
```

### Kubernetes

TODO

## Simulate Data with the `emulate` Directory

You will need to export your environmental variables 