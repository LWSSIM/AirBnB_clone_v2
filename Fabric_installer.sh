#!/bin/bash
# Install Fabric3 and its dependencies (for webservers)

pip3 uninstall -y Fabric

sudo apt-get update
sudo apt-get install -y libffi-dev libssl-dev build-essential python3.8-dev libpython3-dev

packages=(
	"pyparsing"
	"appdirs"
	"setuptools==40.1.0"
	"cryptography==2.8"
	"bcrypt==3.1.7"
	"PyNaCl==1.3.0"
	"Fabric3==1.14.post1"
)

# Install Python packages
for package in "${packages[@]}"; do
	pip install --force-reinstall "$package"
done

echo "Installation completed successfully."
