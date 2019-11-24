
#!bin/sh
sudo apt update -y
sudo apt install mongodb -y
sudo apt install python3-flask -y
sudo apt install pymongo -y 
cd /home/ubuntu
git clone https://github.com/GustavoGB/APS1.git
cd APS1
export FLASK_APP=main.py
flask run —host=0.0.0.0

