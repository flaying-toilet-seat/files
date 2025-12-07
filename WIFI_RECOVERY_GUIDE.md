# WiFi Password Recovery Guide
## For When Your Old PC is Broken and You Need the Password

This guide provides multiple methods to recover or access your WiFi password when you don't have it saved on your current computer.

---

## Method 1: Check Your Router's Physical Label

**Best for:** Quick access without any computer tools  
**Success Rate:** High (70-80% of routers have this)

### Steps:
1. **Locate your router** (the box with blinking lights from your ISP)
2. **Check the label** on the:
   - Bottom of the router
   - Back panel of the router
   - Side of the router

3. **Look for these labels:**
   - "WiFi Password" or "Wireless Password"
   - "Network Key" or "Security Key"
   - "WPA Key" or "WPA2-PSK"
   - "Passphrase" or "Pre-Shared Key"
   - "Default WiFi Password"

### Example:
```
SSID/Network Name: MyHomeWiFi
Password/Key: ABC123xyz789
```

---

## Method 2: Access Your Router's Admin Panel

**Best for:** When the default password was changed  
**Tool:** `router_wifi_finder.py` (included in this repo)

### Steps:

1. **Run the router finder tool:**
   ```bash
   python3 router_wifi_finder.py
   ```

2. **The tool will:**
   - Automatically find your router's IP address
   - Open the router admin page in your browser
   - Show you common login credentials

3. **Log into your router:**
   - Try the common credentials shown
   - Or use credentials from the router label
   
4. **Find WiFi settings:**
   - Look for sections named:
     - "Wireless Settings" / "WiFi Settings"
     - "Security" / "Wireless Security"
     - "WLAN Configuration"
   
5. **View the password:**
   - The password will be shown (might need to click "Show Password")
   - Usually labeled as "WiFi Password", "Network Key", or "PSK"

### Common Router Login Credentials:

| Brand | IP Address | Username | Password |
|-------|------------|----------|----------|
| Most Routers | 192.168.1.1 | admin | admin |
| Linksys | 192.168.1.1 | admin | admin |
| Netgear | 192.168.1.1 | admin | password |
| TP-Link | 192.168.0.1 | admin | admin |
| D-Link | 192.168.0.1 | admin | (blank) |
| Asus | 192.168.1.1 | admin | admin |
| Belkin | 192.168.2.1 | admin | (blank) |

---

## Method 3: Ask Someone with Access

**Best for:** When you have another device already connected

If you have a phone, tablet, or another computer that's already connected to the WiFi:

### On Their Windows Computer:
```bash
python3 wifi_password_retriever.py
```
(They'll need admin privileges)

### On Their iPhone:
1. Settings → WiFi → (i) next to network name
2. Tap "Password"
3. Use Face ID/Touch ID to view it

### On Their Android:
1. Settings → Network & Internet → WiFi
2. Tap on your network name
3. Tap "Share" (will show QR code and password)

### On Their Mac:
1. Applications → Utilities → Keychain Access
2. Search for the WiFi network name
3. Double-click → Check "Show password"
4. Enter their Mac password to view it

---

## Method 4: Contact Your ISP

**Best for:** When all else fails and the router is from your ISP

### What to do:
1. **Call your Internet Service Provider (ISP)**
2. **Verify your identity** (account number, address, etc.)
3. **They can:**
   - Tell you the current WiFi password
   - Remotely reset it to a new one
   - Guide you through accessing the router

### Common ISPs and Support:
- **Comcast/Xfinity:** 1-800-XFINITY
- **AT&T:** 1-800-288-2020
- **Verizon:** 1-800-VERIZON
- **Spectrum:** 1-855-707-7328
- **CenturyLink:** 1-866-642-0444

---

## Method 5: Reset Router (Last Resort)

**⚠️ WARNING:** This will erase ALL router settings!

### Before You Reset:
- You'll need to set up the router from scratch
- You'll need your ISP account information
- Any custom settings will be lost
- Consider this only if you can't access it any other way

### Steps to Reset:
1. **Locate the reset button** (usually a small hole on the router)
2. **Use a paperclip or pin** to press and hold the button
3. **Hold for 10-30 seconds** until lights blink
4. **Wait for router to restart** (2-3 minutes)
5. **Connect using default credentials** (from router label)
6. **Set up WiFi again** with a new password

---

## Method 6: Use WiFi QR Code Generator

**Best for:** Future reference and easy sharing  
**Tool:** `wifi_qr_generator.py` (included in this repo)

Once you recover your password, generate a QR code:

```bash
python3 wifi_qr_generator.py
```

### Benefits:
- **Easy device setup:** Just scan with phone camera
- **Guest access:** Share without revealing password
- **Print and display:** No more asking for password
- **Works offline:** Once generated, no internet needed

### How to use the QR code:
1. Print it and keep it with your router
2. Put it in a photo frame near your entrance
3. Save it on your phone to share easily

---

## Quick Reference Decision Tree

```
Do you have physical access to the router?
│
├─ YES → Check the router label (Method 1)
│        └─ Found it? ✓ Done!
│        └─ Not found? → Try router admin panel (Method 2)
│
└─ NO → Do you have another device connected?
         │
         ├─ YES → Use that device to retrieve password (Method 3)
         │        └─ Generate QR code for future (Method 6)
         │
         └─ NO → Is the router from your ISP?
                  │
                  ├─ YES → Contact ISP (Method 4)
                  │
                  └─ NO → Consider router reset (Method 5)
                           (Last resort only!)
```

---

## Prevention for the Future

To avoid this situation again:

1. **Save it in a password manager:**
   - LastPass, 1Password, Bitwarden, etc.

2. **Write it down and keep it secure:**
   - In a safe place at home
   - Don't label it "WiFi password" for security

3. **Generate a QR code:**
   - Use `wifi_qr_generator.py`
   - Print and keep with router

4. **Take a photo of the router label:**
   - Save in a secure location on your phone
   - Upload to secure cloud storage

5. **Share with trusted family members:**
   - So others can help if needed

---

## Additional Tools in This Repository

1. **`wifi_password_retriever.py`**
   - Retrieves passwords saved on your current computer
   - Works on Windows, Linux, macOS

2. **`router_wifi_finder.py`**
   - Helps you access your router's admin panel
   - Shows common credentials and IPs

3. **`wifi_qr_generator.py`**
   - Creates QR codes for easy WiFi sharing
   - No more typing passwords!

---

## Troubleshooting Common Issues

### "I can't find the router"
- It's the device connected to your internet modem
- Usually has multiple antennas
- Has blinking lights
- Connected to wall with cable

### "The router label is worn out/unreadable"
- Try Method 2 (router admin panel)
- Contact your ISP (Method 4)

### "Default credentials don't work"
- Someone changed them (common for security)
- Try Method 4 (contact ISP)
- Last resort: Method 5 (reset router)

### "I don't have admin/sudo access"
- Ask your system administrator
- Or use physical label methods
- Contact ISP if it's their router

---

## Security Notes

- **Never share your WiFi password publicly** or with untrusted people
- **Change default router passwords** to improve security
- **Use WPA2 or WPA3 encryption** (not WEP)
- **Consider a guest network** for visitors
- **Regularly update router firmware** for security patches

---

## Need More Help?

If none of these methods work:
1. Check your router manufacturer's website for specific guides
2. Search for your router model + "default password"
3. Visit router manufacturer support forums
4. Consider professional IT help if it's critical
