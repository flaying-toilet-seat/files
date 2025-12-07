# WiFi Password Recovery Tools

> **👉 NEW USER? START HERE → [START_HERE.md](START_HERE.md)**

This repository includes multiple tools to help you recover your WiFi password in different situations.

### 🎯 Which Tool Should I Use?

**Choose based on your situation:**

| Situation | Tool to Use | Command |
|-----------|-------------|---------|
| 💻 **Password saved on THIS computer** | `wifi_password_retriever.py` | See below |
| 🚫 **No router admin access** | `no_admin_access_helper.py` | `python3 no_admin_access_helper.py` |
| 🔧 **Want to access router** | `router_wifi_finder.py` | `python3 router_wifi_finder.py` |
| 📱 **Want to create QR code** | `wifi_qr_generator.py` | `python3 wifi_qr_generator.py` |
| 💔 **Old PC broken, need password on new PC** | See [WIFI_RECOVERY_GUIDE.md](WIFI_RECOVERY_GUIDE.md) | - |

### Features
- **Multiple recovery methods**: Router access, phone check, ISP contact, and more
- **Cross-platform support**: Works on Windows, Linux, and macOS
- **Easy to use**: Simple command-line interface with step-by-step guidance
- **No dependencies**: Uses only Python standard library
- **QR code generation**: Create WiFi QR codes for easy sharing

### Requirements
- Python 3.x (Python 3.6 or newer recommended)
- Admin/sudo privileges (for some tools)
---

## 📚 Detailed Tool Descriptions

### 1. wifi_password_retriever.py
**Retrieves passwords saved on your current computer**

Use this when you need to see WiFi passwords that are already saved on the computer you're using.

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

---

### 2. no_admin_access_helper.py
**⭐ Use this when you DON'T have router admin access**

This interactive tool guides you through ALL alternative methods to recover your WiFi password when you can't access the router admin panel.

```bash
python3 no_admin_access_helper.py
```

**What it helps with:**
- ✅ Checking connected phones/devices
- ✅ Finding password on router label  
- ✅ Retrieving from other computers
- ✅ Contacting ISP for help
- ✅ Safe router reset (last resort)

---

### 3. router_wifi_finder.py
**Access your router's admin panel**

This tool helps you find and access your router's configuration page where you can view/change the WiFi password.

```bash
python3 router_wifi_finder.py
```

**What it does:**
- Automatically detects your router's IP address
- Opens the router admin page in your browser
- Shows common login credentials
- Provides instructions for finding WiFi password in router settings

---

### 4. wifi_qr_generator.py  
**Create QR codes for easy WiFi sharing**

Generate a QR code that others can scan with their phone to connect automatically.

```bash
python3 wifi_qr_generator.py
```

**Benefits:**
- No need to type long passwords
- Easy guest access
- Print and display for visitors
- Works offline once generated

**Optional dependency for image QR codes:**
```bash
pip install qrcode[pil]
```
(Script works without this - provides ASCII QR code or online alternatives)

---

## 📖 Complete Guides

- **[WIFI_RECOVERY_GUIDE.md](WIFI_RECOVERY_GUIDE.md)** - Comprehensive guide for all recovery scenarios
- **[QUICK_START.md](QUICK_START.md)** - Quick reference for each tool

---

### How wifi_password_retriever.py Works

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