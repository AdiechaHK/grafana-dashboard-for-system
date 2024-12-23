# Setup MongoDB Exporter

## Download
```bash
wget https://github.com/percona/mongodb_exporter/releases/download/v0.40.0/mongodb_exporter-0.40.0.linux-amd64.tar.gz
```

## Extract and move to /usr/local/bin
```bash
tar xvf mongodb_exporter-*.tar.gz
sudo mv mongodb_exporter-*/mongodb_exporter /usr/local/bin/
```

## Create systemd service
```bash
sudo tee /etc/systemd/system/mongodb-exporter.service<<EOF
[Unit]
Description=MongoDB Exporter
After=network.target

[Service]
Type=simple
User=mongodb-exporter
Environment="MONGODB_URI=mongodb://localhost:27017"
ExecStart=/usr/local/bin/mongodb_exporter

[Install]
WantedBy=multi-user.target
EOF
```

## Create user
```bash
sudo useradd -rs /bin/false mongodb-exporter
```

## Start service
```bash
sudo systemctl daemon-reload
sudo systemctl start mongodb-exporter
sudo systemctl enable mongodb-exporter
```