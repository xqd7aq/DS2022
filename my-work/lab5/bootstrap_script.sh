#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3
sudo apt-get install -y git
sudo apt-get install -y nginx

#just for trial purposes
sudo apt-get install -y mysql-server
sudo systemctl enable mysql
sudo systemctl start mysql
