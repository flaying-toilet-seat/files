# Quick Start Guide - WiFi Password Retriever

## Windows Users

1. Open **Command Prompt** or **PowerShell** as Administrator:
   - Press `Win + X`
   - Select "Command Prompt (Admin)" or "PowerShell (Admin)"

2. Navigate to the script location:
   ```cmd
   cd path\to\files
   ```

3. Run the script:
   ```cmd
   python wifi_password_retriever.py
   ```

## Linux Users

1. Open Terminal

2. Navigate to the script location:
   ```bash
   cd /path/to/files
   ```

3. Run with sudo:
   ```bash
   sudo python3 wifi_password_retriever.py
   ```

4. Enter your password when prompted

## macOS Users

1. Open Terminal

2. Navigate to the script location:
   ```bash
   cd /path/to/files
   ```

3. Run the script:
   ```bash
   python3 wifi_password_retriever.py
   ```

4. You'll be prompted to enter your login password for each network

---

## What This Tool Does

This script retrieves WiFi passwords that are **already saved** on your computer. It:

✅ Accesses your system's saved WiFi credentials
✅ Works on Windows, Linux, and macOS
✅ Requires no internet connection
✅ Uses only built-in system commands

❌ Does NOT hack or crack WiFi networks
❌ Does NOT access networks you haven't connected to
❌ Does NOT work on networks your computer hasn't saved

## Common Issues

### "Access Denied" or "Permission Denied"
**Solution**: Make sure you're running with administrator/sudo privileges

### "Python not found"
**Solution**: Install Python 3 from [python.org](https://www.python.org/downloads/)

### "No WiFi profiles found"
**Possible reasons**:
- Your computer hasn't saved any WiFi networks
- On Linux: Your system might use a different network manager than NetworkManager

---

## Security Note

This tool is designed to help you recover WiFi passwords for networks **you own or have permission to access**. It only retrieves passwords that are already stored on your own computer.
