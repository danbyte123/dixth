#!/bin/bash

BINARY_URL="https://github.com/danbyte123/dixth/releases/download/ditxh/tool"
INSTALL_DIR="/usr/local/bin"
BINARY_NAME="ditxh"

install_ditxh() {
    # Check if the script is run as root
    if [ "$EUID" -ne 0 ]; then
        echo "Please run this script with sudo or as root."
        exit 1
    fi

    # Download the binary using curl
    echo "Downloading ditxh..."
    curl -L "$BINARY_URL" -o "$INSTALL_DIR/$BINARY_NAME"

    # Make the binary executable
    chmod +x "$INSTALL_DIR/$BINARY_NAME"

    # Verify installation
    if [ -f "$INSTALL_DIR/$BINARY_NAME" ]; then
        echo "ditxh installed successfully!"
        echo "You can now run 'ditxh' from anywhere."
    else
        echo "Installation failed. Please try again."
        exit 1
    fi
}

uninstall_ditxh() {
    # Check if the script is run as root
    if [ "$EUID" -ne 0 ]; then
        echo "Please run this script with sudo or as root."
        exit 1
    fi

    # Remove the binary
    if [ -f "$INSTALL_DIR/$BINARY_NAME" ]; then
        rm "$INSTALL_DIR/$BINARY_NAME"
        echo "$BINARY_NAME uninstalled successfully!"
    else
        echo "$BINARY_NAME is not installed."
    fi
}

# Main logic
if [ "$1" == "uninstall" ]; then
    uninstall_ditxh
else
    install_ditxh
fi
