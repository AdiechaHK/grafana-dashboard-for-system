# Grafana Dashboard Setup

## Setup Exporters
Make sure all the required exporters are running fine and ready to send metrics

* [RabbitMQ](SetupRabbitMqExporter.md)
* [Node - Linux Server](SetupNodeExporter.md)
* [MongoDB](SetupMongoExporter.md)

## Run Prometheus And Grafana
To run these we already setup this on `docker-compose.yml` file, so you just need to make it up and running

```bash
docker compose up -d
```

## Grafana
Now we can start grafana using the following credentials
Username: `admin`
Password: `admin`

## Create Dashboard
Now we can go to `Dashboard` -> `Import` -> following

* Node Exporter Full (ID: `1860`): Comprehensive system metrics
* Node Exporter: Quickstart and Dashboard (ID: `13978`): Simple overview
* RabbitMQ Dashboard (ID: `10991`)
* MongoDB Cluster (ID: `14792`)
* MongoDB Overview (ID: `7353`)



