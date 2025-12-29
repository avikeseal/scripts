#!usr/bin/env bash 

#update package lists:
sudo apt update

#upgrade all installed packages:
sudo apt upgrade -y

#remove unnecessary packages:
sudo apt autoremove -y

#clean up package cache:
sudo apt clean

echo "============================system update and cleanup complete===================================="
