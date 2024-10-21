# Installation Guide

This document provides instructions on how to install Python and various packages needed to review the code that we used in our Python Network Sniffer project.

## Prerequisites

Ensure that you have administrative privileges on your machine to install software.

1. **For Debian/Ubuntu-based systems** (including Kali Linux):
   Open your terminal and run:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
2. **Install Scapy, bandit,black and pylint**
 ```bash
pip install scapy
pip install bandit
pip install black
pip install pylint
3. **To run these on your code directory, navigate to your project folder and execute,**
for example,
 ```bash
 bandit -r /path/to/your/code/
Replace /path/to/your/code/ with the actual path to your Python files.
