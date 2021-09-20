#!/bin/bash
sudo apt-get install docker docker-compose -y
sudo service docker start
sudo usermod -a -G docker "$USER"
sudo chmod 666 /var/run/docker.sock
sudo service docker start