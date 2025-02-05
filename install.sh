#!/bin/bash

 
BINARY_URL="https://github.com/danbyte123/dixth.git"

 
INSTALL_DIR="/usr/local/bin"

 
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script with sudo or as root."
  exit 1
fi

 
echo "Downloading ditxh..."
curl -L "$BINARY_URL" -o "$INSTALL_DIR/ditxh"

 
chmod +x "$INSTALL_DIR/ditxh"

 
if [ -f "$INSTALL_DIR/ditxh" ]; then
  echo "ditxh installed successfully!"
  echo "You can now run 'ditxh' from anywhere."
else
  echo "Installation failed. Please try again."
  exit 1
fi
