#!/bin/bash

BINARY_URL="https://github.com/danbyte123/dixth/releases/latest/download/ditxh"
INSTALL_DIR="/usr/local/bin"
BINARY_NAME="ditxh"

install_ditxh() {
    if [ "$EUID" -ne 0 ]; then
        echo "Please run this script with sudo or as root."
        exit 1
    fi

    echo "Downloading ditxh..."
    wget -O "$INSTALL_DIR/$BINARY_NAME" "$BINARY_URL"

    chmod +x "$INSTALL_DIR/$BINARY_NAME"

    if [ -f "$INSTALL_DIR/$BINARY_NAME" ]; then
        echo "ditxh installed successfully!"
        echo "You can now run 'ditxh' from anywhere."
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
