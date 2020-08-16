#! /bin/bash

echo ""
echo "installing dependencies :"
echo "-------------------------"
echo ""

sudo apt-get install can-utils

echo ""
echo "updating your system :"
echo "----------------------"
echo ""

v=sudo apt-get update && sudo apt-get dist-upgrade
$v
