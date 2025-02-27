#!/bin/bash

BINARY_URL="https://github.com/danbyte123/dixth/releases/download/ditxh/tool.bin"
INSTALL_DIR="/usr/local/bin"
BINARY_NAME="ditxh"

install_ditxh() {
     
    if [ "$EUID" -ne 0 ]; then
        echo "Please run this script with sudo or as root."
        exit 1
    fi

    
    echo "Downloading ditxh..."
    curl -L "$BINARY_URL" -o "$INSTALL_DIR/$BINARY_NAME"

     
    chmod +x "$INSTALL_DIR/$BINARY_NAME"

 
    if [ -f "$INSTALL_DIR/$BINARY_NAME" ]; then
        echo "ditxh installed successfully!"
         
    else
        echo "Installation failed. Please try again."
        exit 1
    fi
}

uninstall_ditxh() {
     
    if [ "$EUID" -ne 0 ]; then
        echo "Please run this script with sudo or as root."
        exit 1
    fi

   
    if [ -f "$INSTALL_DIR/$BINARY_NAME" ]; then
        rm "$INSTALL_DIR/$BINARY_NAME"
        echo "$BINARY_NAME uninstalled successfully!"
    else
        echo "$BINARY_NAME is not installed."
    fi
}

 
if [ "$1" == "uninstall" ]; then
    uninstall_ditxh
else
    install_ditxh
fi
