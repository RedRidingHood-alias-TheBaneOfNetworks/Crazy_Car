#! /bin/bash

echo ""
echo "updating your system :"
echo "-----------------------"
echo ""
sudo apt-get update && sudo apt-get dist-upgrade

echo ""
echo "installing dependencies :"
echo "--------------------------"
echo ""
sudo apt-get install can-utils
