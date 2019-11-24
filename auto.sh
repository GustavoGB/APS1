
#!bin/sh
sudo apt update -y
sudo apt install python3-pip -y
sudo apt install mongodb -y
cd /home/ubuntu
git clone https://github.com/GustavoGB/APS1.git
cd APS1
sudo pip install -r requirements.txt
python3 main.py

