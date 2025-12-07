#!/usr/bin/env python3
"""
WiFi Password Retriever
This script retrieves saved WiFi passwords from your system.
Supports Windows, Linux, and macOS.
"""

import subprocess
import platform
import sys
import re


def get_wifi_passwords_windows():
    """Retrieve WiFi passwords on Windows using netsh command."""
    try:
        # Get list of saved WiFi profiles
        profiles_output = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profiles'],
            encoding='utf-8',
            stderr=subprocess.DEVNULL
        )
        
        # Extract profile names
        profile_names = re.findall(r'All User Profile\s*:\s*(.*)', profiles_output)
        
        if not profile_names:
            print("No WiFi profiles found.")
            return []
        
        wifi_list = []
        print(f"Found {len(profile_names)} WiFi profile(s):\n")
        
        for profile in profile_names:
            profile = profile.strip()
            try:
                # Get password for each profile
                password_output = subprocess.check_output(
                    ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'],
                    encoding='utf-8',
                    stderr=subprocess.DEVNULL
                )
                
                # Extract password
                password_match = re.search(r'Key Content\s*:\s*(.*)', password_output)
                password = password_match.group(1) if password_match else "No password found"
                
                wifi_list.append({'ssid': profile, 'password': password})
                print(f"SSID: {profile}")
                print(f"Password: {password}")
                print("-" * 50)
                
            except subprocess.CalledProcessError:
                print(f"SSID: {profile}")
                print(f"Password: Unable to retrieve")
                print("-" * 50)
        
        return wifi_list
        
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to retrieve WiFi profiles. Make sure you run this with administrator privileges.")
        print(f"Details: {e}")
        return []
    except FileNotFoundError:
        print("Error: 'netsh' command not found. This might not be a Windows system.")
        return []


def get_wifi_passwords_linux():
    """Retrieve WiFi passwords on Linux from NetworkManager."""
    try:
        # Check for NetworkManager
        nm_path = "/etc/NetworkManager/system-connections/"
        
        print("Reading WiFi passwords from NetworkManager...\n")
        print("Note: You need root/sudo privileges to access saved passwords.\n")
        
        # List connection files
        try:
            connections = subprocess.check_output(
                ['sudo', 'ls', nm_path],
                encoding='utf-8',
                stderr=subprocess.DEVNULL
            )
            
            connection_files = connections.strip().split('\n')
            
            if not connection_files or connection_files == ['']:
                print("No WiFi profiles found.")
                return []
            
            wifi_list = []
            print(f"Found {len(connection_files)} connection(s):\n")
            
            for connection_file in connection_files:
                try:
                    # Read connection file
                    content = subprocess.check_output(
                        ['sudo', 'cat', f"{nm_path}{connection_file}"],
                        encoding='utf-8',
                        stderr=subprocess.DEVNULL
                    )
                    
                    # Extract SSID
                    ssid_match = re.search(r'ssid\s*=\s*(.*)', content)
                    ssid = ssid_match.group(1) if ssid_match else connection_file
                    
                    # Extract password (psk for WPA/WPA2)
                    password_match = re.search(r'psk\s*=\s*(.*)', content)
                    password = password_match.group(1) if password_match else "No password found or Open network"
                    
                    wifi_list.append({'ssid': ssid, 'password': password})
                    print(f"SSID: {ssid}")
                    print(f"Password: {password}")
                    print("-" * 50)
                    
                except subprocess.CalledProcessError:
                    print(f"Unable to read: {connection_file}")
                    print("-" * 50)
            
            return wifi_list
            
        except subprocess.CalledProcessError:
            print("Error: Unable to access NetworkManager connections.")
            print("Make sure you run this script with sudo privileges:")
            print("  sudo python3 wifi_password_retriever.py")
            return []
            
    except Exception as e:
        print(f"Error retrieving WiFi passwords on Linux: {e}")
        return []


def get_wifi_passwords_macos():
    """Retrieve WiFi passwords on macOS using security command."""
    try:
        # Get list of preferred networks
        print("Retrieving WiFi passwords from macOS Keychain...\n")
        print("Note: You'll be prompted to enter your login password for each network.\n")
        
        # Get list of WiFi networks
        airport_output = subprocess.check_output(
            ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'],
            encoding='utf-8',
            stderr=subprocess.DEVNULL
        )
        
        # Extract SSIDs
        ssids = []
        for line in airport_output.split('\n')[1:]:  # Skip header
            if line.strip():
                parts = line.split()
                if parts:
                    ssids.append(parts[0])
        
        # Also try to get known networks from preferences
        try:
            known_networks_output = subprocess.check_output(
                ['networksetup', '-listpreferredwirelessnetworks', 'en0'],
                encoding='utf-8',
                stderr=subprocess.DEVNULL
            )
            for line in known_networks_output.split('\n')[1:]:  # Skip header
                if line.strip():
                    ssid = line.strip()
                    if ssid not in ssids:
                        ssids.append(ssid)
        except:
            pass
        
        if not ssids:
            print("No WiFi networks found.")
            return []
        
        wifi_list = []
        print(f"Found {len(ssids)} network(s). Attempting to retrieve passwords...\n")
        
        for ssid in ssids:
            try:
                # Get password from keychain
                password_output = subprocess.check_output(
                    ['security', 'find-generic-password', '-ga', ssid],
                    encoding='utf-8',
                    stderr=subprocess.STDOUT
                )
                
                # Extract password
                password_match = re.search(r'password: "(.*)"', password_output)
                password = password_match.group(1) if password_match else "Unable to retrieve"
                
                wifi_list.append({'ssid': ssid, 'password': password})
                print(f"SSID: {ssid}")
                print(f"Password: {password}")
                print("-" * 50)
                
            except subprocess.CalledProcessError:
                print(f"SSID: {ssid}")
                print(f"Password: Unable to retrieve (may require authorization)")
                print("-" * 50)
        
        return wifi_list
        
    except Exception as e:
        print(f"Error retrieving WiFi passwords on macOS: {e}")
        return []


def main():
    """Main function to detect OS and retrieve WiFi passwords."""
    print("=" * 50)
    print("WiFi Password Retriever")
    print("=" * 50)
    print()
    
    system = platform.system()
    
    if system == "Windows":
        print("Detected Windows system.\n")
        wifi_passwords = get_wifi_passwords_windows()
    elif system == "Linux":
        print("Detected Linux system.\n")
        wifi_passwords = get_wifi_passwords_linux()
    elif system == "Darwin":
        print("Detected macOS system.\n")
        wifi_passwords = get_wifi_passwords_macos()
    else:
        print(f"Unsupported operating system: {system}")
        sys.exit(1)
    
    if wifi_passwords:
        print(f"\n{'=' * 50}")
        print(f"Total passwords retrieved: {len(wifi_passwords)}")
        print(f"{'=' * 50}")
    else:
        print("\nNo WiFi passwords were retrieved.")
        print("This could be due to:")
        print("  - Insufficient privileges (try running as admin/sudo)")
        print("  - No saved WiFi profiles on this system")
        print("  - System configuration differences")


if __name__ == "__main__":
    main()
