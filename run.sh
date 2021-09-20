#!/bin/bash
cd /home/ubuntu/d1-bot || return
docker-compose build --no-cache
docker-compose up -d