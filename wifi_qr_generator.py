#!/usr/bin/env python3
"""
WiFi QR Code Generator
Generate QR codes for easy WiFi sharing - useful when setting up new devices
or sharing WiFi with guests without revealing the password.

This script can work with or without the qrcode library:
- With qrcode: Generates actual QR code images
- Without qrcode: Generates ASCII art QR codes or provides URLs
"""

import sys


def escape_wifi_string(text):
    """Escape special characters for WiFi QR code format."""
    return text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace(":", "\\:")


def generate_wifi_string(ssid, password, security="WPA"):
    """
    Generate WiFi configuration string in the standard format.
    Format: WIFI:T:<security>;S:<ssid>;P:<password>;H:<hidden>;;
    """
    # Escape special characters
    ssid = escape_wifi_string(ssid)
    password = escape_wifi_string(password)
    
    wifi_string = f"WIFI:T:{security};S:{ssid};P:{password};;"
    return wifi_string


def generate_qr_with_library(wifi_string, filename="wifi_qr.png"):
    """Generate QR code using qrcode library."""
    try:
        import qrcode
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(wifi_string)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        
        return True, filename
    except ImportError:
        return False, "qrcode library not installed"


def generate_qr_ascii(wifi_string):
    """Generate ASCII art QR code using qrcode library."""
    try:
        import qrcode
        
        qr = qrcode.QRCode(border=1)
        qr.add_data(wifi_string)
        qr.make(fit=True)
        
        # Generate ASCII art
        print("\nQR Code (ASCII):")
        print("=" * 60)
        qr.print_ascii(invert=True)
        print("=" * 60)
        return True
    except ImportError:
        return False


def provide_online_qr_options(wifi_string):
    """Provide online QR code generation options."""
    print("\nOnline QR Code Generators:")
    print("-" * 70)
    print("\nYou can use these websites to generate a QR code:")
    print("\n1. QR Code Generator (https://www.qr-code-generator.com/)")
    print("   - Go to the website")
    print("   - Select 'WiFi' option")
    print("   - Enter your WiFi details")
    print("   - Generate and download the QR code")
    
    print("\n2. QiFi (https://qifi.org/)")
    print("   - Simple WiFi QR code generator")
    print("   - Enter your network details")
    print("   - Download or print the QR code")
    
    print("\n3. Manual QR Code:")
    print("   - Use any QR code generator")
    print("   - Encode this string:")
    print()
    print(f"   {wifi_string}")
    print()


def install_qrcode_library():
    """Provide instructions to install qrcode library."""
    print("\nTo generate QR code images, install the qrcode library:")
    print("-" * 70)
    print("\nOption 1 - Install qrcode with image support:")
    print("  pip install qrcode[pil]")
    print("\nOption 2 - Install qrcode without image (ASCII only):")
    print("  pip install qrcode")
    print()


def main():
    """Main function to generate WiFi QR code."""
    print("=" * 70)
    print("WiFi QR Code Generator")
    print("=" * 70)
    print()
    print("This tool generates QR codes for easy WiFi sharing.")
    print("Scan the QR code with a phone to connect automatically!")
    print()
    
    # Get WiFi details
    ssid = input("Enter WiFi network name (SSID): ").strip()
    if not ssid:
        print("Error: SSID cannot be empty.")
        sys.exit(1)
    
    password = input("Enter WiFi password: ").strip()
    
    print("\nSecurity type:")
    print("  1. WPA/WPA2 (most common)")
    print("  2. WEP (old, not recommended)")
    print("  3. No password (open network)")
    
    security_choice = input("Choose security type (1-3, default: 1): ").strip()
    
    if security_choice == "2":
        security = "WEP"
    elif security_choice == "3":
        security = "nopass"
        password = ""
    else:
        security = "WPA"
    
    # Generate WiFi string
    wifi_string = generate_wifi_string(ssid, password, security)
    
    print()
    print("=" * 70)
    print("WiFi Configuration String:")
    print(wifi_string)
    print("=" * 70)
    print()
    
    # Try to generate QR code
    print("Generating QR code...")
    print("-" * 70)
    
    # Try with image
    success, result = generate_qr_with_library(wifi_string)
    
    if success:
        print(f"✓ QR code image saved as: {result}")
        print("  You can now print or share this image!")
        print()
        
        # Also try ASCII version
        if generate_qr_ascii(wifi_string):
            print("\n✓ ASCII QR code displayed above")
            print("  This can be scanned from the screen!")
    else:
        print("! QR code library not installed")
        print()
        
        # Try ASCII only
        if not generate_qr_ascii(wifi_string):
            # No library available, provide alternatives
            install_qrcode_library()
            provide_online_qr_options(wifi_string)
    
    print()
    print("How to use the QR code:")
    print("-" * 70)
    print("""
1. On iPhone/iPad:
   - Open Camera app
   - Point at the QR code
   - Tap the notification to connect

2. On Android:
   - Open Camera app or QR scanner
   - Point at the QR code
   - Tap to connect

3. Print and share:
   - Print the QR code image
   - Display it where guests can scan it
   - No need to share the actual password!
    """)
    
    print("=" * 70)


if __name__ == "__main__":
    main()
