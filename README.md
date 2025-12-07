# files

## WiFi Password Retriever

This repository includes a Python script to help you retrieve saved WiFi passwords from your computer.

### Features
- **Cross-platform support**: Works on Windows, Linux, and macOS
- **Easy to use**: Simple command-line interface
- **No dependencies**: Uses only Python standard library

### Requirements
- Python 3.x (Python 3.6 or newer recommended)

### Usage

#### Windows
Run Command Prompt or PowerShell as **Administrator**:
```bash
python wifi_password_retriever.py
```

#### Linux
Run with **sudo** privileges:
```bash
sudo python3 wifi_password_retriever.py
```

Note: This script reads from NetworkManager's system connections. If your system uses a different network manager, the script may need adjustments.

#### macOS
Run the script normally (you'll be prompted for your login password):
```bash
python3 wifi_password_retriever.py
```

Note: You may need to authorize keychain access for each network.

### How It Works

- **Windows**: Uses the `netsh wlan` command to retrieve saved WiFi profiles and their passwords
- **Linux**: Reads from NetworkManager's configuration files in `/etc/NetworkManager/system-connections/`
- **macOS**: Queries the macOS Keychain using the `security` command

### Important Notes

1. **Administrator/Root Privileges**: Most operating systems require elevated privileges to access saved WiFi passwords for security reasons.

2. **Security**: This script only accesses passwords that are already saved on your computer. It does not crack or hack any networks.

3. **Permissions**: You may need to grant permissions when running the script, especially on macOS.

### Example Output

```
==================================================
WiFi Password Retriever
==================================================

Detected Windows system.

Found 3 WiFi profile(s):

SSID: HomeNetwork
Password: MySecurePassword123
--------------------------------------------------
SSID: OfficeWiFi
Password: CompanyPassword456
--------------------------------------------------
SSID: GuestNetwork
Password: Guest2023
--------------------------------------------------

==================================================
Total passwords retrieved: 3
==================================================
```

### Troubleshooting

**"Access denied" or "Permission denied"**
- Make sure you're running the script with administrator/sudo privileges

**"No WiFi profiles found"**
- Your computer may not have any saved WiFi networks
- On Linux, your system might use a different network manager

**"Command not found"**
- Ensure Python 3 is installed on your system
- Try using `python` instead of `python3` or vice versa

### License

This tool is provided as-is for personal use to recover your own WiFi passwords.