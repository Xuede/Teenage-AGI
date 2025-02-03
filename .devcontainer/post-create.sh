#!/bin/bash

# Update package lists
sudo apt-get update

# Install sqlite3
sudo apt-get install -y sqlite3

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt