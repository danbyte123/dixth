#!/bin/bash

# Define the URL of the binary
BINARY_URL="https://github.com/yourusername/your-repo-name/releases/latest/download/ditxh"

# Define the installation directory
INSTALL_DIR="/usr/local/bin"

# Check if the user has sudo privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script with sudo or as root."
  exit 1
fi

# Download the binary
echo "Downloading ditxh..."
curl -L "$BINARY_URL" -o "$INSTALL_DIR/ditxh"

# Make the binary executable
chmod +x "$INSTALL_DIR/ditxh"

# Verify installation
if [ -f "$INSTALL_DIR/ditxh" ]; then
  echo "ditxh installed successfully!"
  echo "You can now run 'ditxh' from anywhere."
else
  echo "Installation failed. Please try again."
  exit 1
fi
