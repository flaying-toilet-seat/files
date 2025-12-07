#!/usr/bin/env python3
"""
Router WiFi Password Finder
This script helps you find your WiFi password by accessing your router,
useful when you don't have it saved on any computer.
"""

import webbrowser
import socket
import subprocess
import platform
import sys
import re


def get_default_gateway():
    """Get the default gateway (router) IP address."""
    system = platform.system()
    
    try:
        if system == "Windows":
            # Use ipconfig on Windows
            result = subprocess.check_output(['ipconfig'], encoding='utf-8')
            # Look for Default Gateway
            matches = re.findall(r'Default Gateway.*?:\s*(\d+\.\d+\.\d+\.\d+)', result)
            if matches:
                return matches[0]
        
        elif system in ["Linux", "Darwin"]:
            # Use ip route or route on Linux/macOS
            try:
                result = subprocess.check_output(['ip', 'route'], encoding='utf-8')
                match = re.search(r'default via (\d+\.\d+\.\d+\.\d+)', result)
                if match:
                    return match.group(1)
            except FileNotFoundError:
                # Fallback to netstat command (more portable)
                result = subprocess.check_output(['netstat', '-rn'], encoding='utf-8')
                # Look for default route
                for line in result.split('\n'):
                    if 'default' in line.lower() or '0.0.0.0' in line:
                        parts = line.split()
                        for part in parts:
                            if re.match(r'\d+\.\d+\.\d+\.\d+', part) and part != '0.0.0.0':
                                return part
                                break
    
    except subprocess.CalledProcessError:
        pass
    
    return None


def get_common_router_ips():
    """Return a list of common router IP addresses."""
    return [
        "192.168.1.1",
        "192.168.0.1",
        "192.168.1.254",
        "192.168.2.1",
        "10.0.0.1",
        "10.0.1.1",
        "192.168.100.1",
        "192.168.10.1",
        "192.168.11.1",
        "192.168.3.1",
    ]


def get_common_credentials():
    """Return common router login credentials."""
    return [
        ("admin", "admin"),
        ("admin", "password"),
        ("admin", ""),
        ("admin", "1234"),
        ("root", "admin"),
        ("root", "root"),
        ("admin", "admin123"),
        ("user", "user"),
        ("", "admin"),
        ("", ""),
    ]


def test_router_connection(ip):
    """Test if router is accessible at given IP."""
    try:
        socket.create_connection((ip, 80), timeout=2)
        return True
    except (socket.timeout, socket.error, ConnectionRefusedError):
        pass
    
    # Try HTTPS port
    try:
        socket.create_connection((ip, 443), timeout=2)
        return True
    except (socket.timeout, socket.error, ConnectionRefusedError):
        pass
    
    return False


def open_router_admin(ip):
    """Open router admin page in browser."""
    urls = [
        f"http://{ip}",
        f"https://{ip}",
    ]
    
    print(f"Opening router admin page at {ip}...")
    webbrowser.open(urls[0])
    return True


def main():
    """Main function to help user find WiFi password from router."""
    print("=" * 70)
    print("Router WiFi Password Finder")
    print("=" * 70)
    print()
    print("This tool helps you find your WiFi password by accessing your router.")
    print("Useful when your old PC is broken and you need the password on a new PC.")
    print()
    
    # Step 1: Find router IP
    print("Step 1: Finding your router's IP address...")
    print("-" * 70)
    
    gateway_ip = get_default_gateway()
    
    if gateway_ip:
        print(f"✓ Found router IP: {gateway_ip}")
        router_ip = gateway_ip
    else:
        print("! Could not automatically detect router IP.")
        print("\nCommon router IP addresses:")
        common_ips = get_common_router_ips()
        for i, ip in enumerate(common_ips, 1):
            print(f"  {i}. {ip}")
        
        router_ip = common_ips[0]  # Default to most common
    
    print()
    
    # Step 2: Test connection
    print("Step 2: Testing connection to router...")
    print("-" * 70)
    
    if test_router_connection(router_ip):
        print(f"✓ Router is accessible at {router_ip}")
    else:
        print(f"! Could not connect to router at {router_ip}")
        print("  The router might be at a different IP address.")
    
    print()
    
    # Step 3: Router login information
    print("Step 3: Router Login Information")
    print("-" * 70)
    print("Common default router credentials:")
    print()
    
    credentials = get_common_credentials()
    print("Username       | Password")
    print("-" * 40)
    for username, password in credentials[:8]:
        user_display = username if username else "(blank)"
        pass_display = password if password else "(blank)"
        print(f"{user_display:14} | {pass_display}")
    
    print()
    print("NOTE: If these don't work, check the sticker on your router!")
    print()
    
    # Step 4: Instructions
    print("Step 4: How to Find Your WiFi Password in Router Settings")
    print("-" * 70)
    print("""
Once you log into your router, look for these sections:
  • Wireless Settings / WiFi Settings / WLAN Settings
  • Security Settings
  • Wireless Security
  • WiFi Configuration
  
The password might be labeled as:
  • WiFi Password / Wireless Password
  • Network Key / Security Key
  • Passphrase / Pre-Shared Key (PSK)
  • WPA/WPA2 Password
    """)
    
    print()
    print("Step 5: Alternative Methods")
    print("-" * 70)
    print("""
If you can't access the router admin panel:

1. CHECK THE ROUTER LABEL:
   - Most routers have a sticker with default WiFi password
   - Look on the bottom or back of the router
   - It may say "WiFi Password", "Network Key", or "WPA Key"

2. CHECK THE ROUTER BOX/MANUAL:
   - The original packaging often includes the password
   - Check any documentation that came with the router

3. CONTACT YOUR ISP:
   - If the router was provided by your Internet Service Provider
   - They can help you reset or retrieve the password

4. RESET THE ROUTER (Last Resort):
   - Press and hold the reset button for 10-30 seconds
   - This will reset ALL settings including the password
   - You'll need to set up the router again from scratch
    """)
    
    print()
    
    # Step 6: Open browser
    response = input("Would you like to open your router's admin page now? (y/n): ")
    
    if response.lower() in ['y', 'yes']:
        open_router_admin(router_ip)
        print()
        print("✓ Browser opened. Log in with the credentials shown above.")
        print()
        print(f"If the page doesn't load, your router might be at a different IP.")
        print(f"Try these URLs manually:")
        for ip in get_common_router_ips()[:5]:
            print(f"  - http://{ip}")
    else:
        print()
        print(f"You can manually visit: http://{router_ip}")
    
    print()
    print("=" * 70)
    print("Good luck finding your WiFi password!")
    print("=" * 70)


if __name__ == "__main__":
    main()
