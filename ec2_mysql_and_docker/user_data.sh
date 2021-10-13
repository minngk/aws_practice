#!/bin/bash
sudo yum -y update
sudo yum install -y mysql
sudo yum install -y docker
sudo systemctl start docker
sudo usermod -a -G docker ec2-user
sudo systemctl enable docker 