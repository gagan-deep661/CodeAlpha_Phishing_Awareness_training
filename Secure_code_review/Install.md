# Installation Guide

This document provides instructions on how to install Python and various packages needed to review the code that we used in our Python Network Sniffer project.

## Prerequisites

Ensure that you have administrative privileges on your machine to install software.

1. **For Debian/Ubuntu-based systems** (including Kali Linux):
   Open your terminal and run:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
2. **Install Scapy, bandit,black and pylint and run to review the code**
 ```bash
pip install scapy
pip install bandit
pip install black
pip install pylint
black /path/to/your/code.py
pylint /path/to/your/code.py

Ensure that you replace /path/to/your/code.py with the actual path to the specific Python file you want to analyze or format.
