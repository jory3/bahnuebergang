#!/bin/bash
cd "/home/pi/projects/bahnuebergang/"
sudo cp barriere.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/barriere.service
chmod +x /home/pi/projects/bahnuebergang/main.py
sudo systemctl daemon-reload
sudo systemctl enable barriere.service
sudo systemctl start barriere.service
