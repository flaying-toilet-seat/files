#!/usr/bin/env python3
"""
WiFi Password Recovery - No Router Admin Access
This script helps you recover your WiFi password when you CAN'T access the router admin panel.
"""

import sys
import platform
import subprocess


def check_phone_connected():
    """Guide user to check if they have a phone connected."""
    print("\n" + "=" * 70)
    print("METHOD 1: Check Your Phone (If Connected to WiFi)")
    print("=" * 70)
    print("""
If you have a smartphone that's already connected to the WiFi:

📱 ON ANDROID (Easiest):
   1. Open Settings → Network & Internet → WiFi
   2. Tap on your connected network name
   3. Tap "Share" or "QR Code" button
   4. The password will be shown below the QR code!
   
   Alternative (Some Android versions):
   1. Settings → WiFi → Tap on network name
   2. Look for "Show password" checkbox
   3. Check the box to reveal password

📱 ON iPHONE (iOS 16 or newer):
   1. Open Settings → WiFi
   2. Tap the (i) icon next to your network
   3. Tap "Password" field
   4. Use Face ID/Touch ID to view the password
   5. Tap the password to copy it

📱 ON iPHONE (Older iOS):
   Unfortunately, older iPhones don't show WiFi passwords easily.
   You'll need to use a Mac or another method.

🖥️ ON MAC (If you've connected before):
   1. Open "Keychain Access" (in Applications → Utilities)
   2. In the search box, type your WiFi network name
   3. Double-click the network name in results
   4. Check "Show password" checkbox
   5. Enter your Mac login password
   6. Password will be revealed!
""")
    
    response = input("Do you have a phone or device connected to this WiFi? (y/n): ")
    return response.lower() in ['y', 'yes']


def check_router_label():
    """Guide user to check router label."""
    print("\n" + "=" * 70)
    print("METHOD 2: Check Your Router's Physical Label")
    print("=" * 70)
    print("""
Most routers have the WiFi password printed on a sticker/label.

🔍 WHERE TO LOOK:
   • Bottom of the router (most common)
   • Back panel of the router
   • Side of the router
   • Inside the battery compartment (for portable routers)

📝 WHAT TO LOOK FOR:
   The password might be labeled as:
   • "WiFi Password" or "Wireless Password"
   • "Network Key" or "Security Key"  
   • "WPA Key" or "WPA2-PSK"
   • "Passphrase" or "Pre-Shared Key"
   • "Password" next to your network name

📦 ALSO CHECK:
   • The original router box/packaging
   • Any setup cards that came with the router
   • The router's user manual

⚠️ NOTE: If the password was changed from default, the label 
         won't help. Move to the next method.
""")
    
    response = input("Can you physically check your router? (y/n): ")
    return response.lower() in ['y', 'yes']


def check_other_computers():
    """Guide for checking other computers."""
    print("\n" + "=" * 70)
    print("METHOD 3: Check Other Computers in Your Home")
    print("=" * 70)
    print("""
If you have other computers that are connected to the WiFi,
you can retrieve the password from them.

💻 ON WINDOWS (Need Administrator privileges):
   1. Open Command Prompt as Administrator
      (Right-click Start → "Command Prompt (Admin)" or "PowerShell (Admin)")
   
   2. Run this command:
      netsh wlan show profile name="YOUR_WIFI_NAME" key=clear
   
   3. Look for "Key Content" - that's your password!
   
   Or use our tool:
      python wifi_password_retriever.py

🐧 ON LINUX (Need sudo access):
   1. Open Terminal
   
   2. Run:
      sudo cat /etc/NetworkManager/system-connections/YOUR_WIFI_NAME
   
   3. Look for "psk=" line - that's your password!
   
   Or use our tool:
      sudo python3 wifi_password_retriever.py

🍎 ON MAC:
   Use Method 1 (Phone) instructions for Mac Keychain Access

📱 ON TABLETS/CHROMEBOOKS:
   Same methods as phones (see Method 1)
""")
    
    response = input("Do you have other computers connected to this WiFi? (y/n): ")
    return response.lower() in ['y', 'yes']


def contact_isp_info():
    """Provide ISP contact information."""
    print("\n" + "=" * 70)
    print("METHOD 4: Contact Your Internet Service Provider (ISP)")
    print("=" * 70)
    print("""
If your router was provided by your ISP, they can help!

📞 WHAT YOUR ISP CAN DO:
   • Tell you the current WiFi password
   • Reset your password remotely
   • Guide you through router access
   • Send a technician if needed

🆔 WHAT YOU'LL NEED:
   • Your account number
   • Your name and address
   • Possibly a security PIN or last 4 digits of SSN
   • Router serial number (on router label)

📋 COMMON ISP SUPPORT NUMBERS:

USA:
   • Comcast/Xfinity: 1-800-XFINITY (1-800-934-6489)
   • AT&T: 1-800-288-2020
   • Verizon: 1-800-VERIZON (1-800-837-4966)
   • Spectrum (Charter): 1-855-707-7328
   • Cox: 1-800-234-3993
   • CenturyLink: 1-866-642-0444
   • Frontier: 1-800-921-8101
   • Optimum: 1-866-200-7273

💡 TIP: Call during business hours for faster service.
        Have your account information ready before calling.

🌐 OR: Log into your ISP's website/app
       Many ISPs let you view/change WiFi password online!
""")
    
    response = input("Is your router from your ISP? (y/n): ")
    return response.lower() in ['y', 'yes']


def router_reset_warning():
    """Warn about router reset and provide instructions."""
    print("\n" + "=" * 70)
    print("METHOD 5: Router Reset (⚠️ LAST RESORT ONLY)")
    print("=" * 70)
    print("""
⚠️⚠️⚠️ WARNING - READ CAREFULLY ⚠️⚠️⚠️

Resetting your router will:
   ❌ Erase ALL custom settings
   ❌ Disconnect all devices
   ❌ Reset WiFi name and password to default
   ❌ Require complete router setup again
   ❌ May need ISP account info to reconnect

✅ Only do this if:
   • You've tried ALL other methods
   • You're comfortable setting up the router again
   • You have your ISP account information
   • You can handle all devices disconnecting

📝 BEFORE YOU RESET:
   1. Write down your current WiFi network name
   2. Get your ISP account username/password ready
   3. Have router label info accessible
   4. Warn everyone who uses the WiFi
   5. Check if your ISP offers remote assistance

🔄 HOW TO RESET:
   1. Find the RESET button (small hole on router)
   2. Use a paperclip or pin
   3. Press and HOLD for 10-30 seconds
   4. Watch lights - they'll blink/flash
   5. Wait 2-5 minutes for router to restart
   6. Connect using DEFAULT password from label
   7. Set up WiFi with NEW name and password

💡 BETTER ALTERNATIVE:
   Call your ISP first! They might:
   • Reset it remotely without you doing anything
   • Guide you through a safer process
   • Send a technician to help
""")
    
    print("\n" + "⚠️" * 35)
    response = input("\nDo you want to proceed with router reset? (yes/no): ")
    return response.lower() == 'yes'


def check_ask_neighbors():
    """Option to ask someone who may have set up the router."""
    print("\n" + "=" * 70)
    print("METHOD 6: Ask Who Set Up the Router")
    print("=" * 70)
    print("""
💭 THINK ABOUT:

   • Who set up the router initially?
   • Did a friend/family member help with setup?
   • Did a technician install it?
   • Landlord? (if renting)
   • Previous roommate?
   • IT person at work? (if work WiFi)

These people might:
   ✓ Remember the password
   ✓ Have it written down
   ✓ Know where it's documented
   ✓ Have access to accounts that show it

💡 ALSO CHECK:
   • Shared password managers (LastPass, 1Password, etc.)
   • Shared notes (Evernote, OneNote, Google Keep)
   • Family/household documentation
   • Email from ISP about router setup
   • Text messages about WiFi password
""")
    
    input("\nPress Enter to continue...")


def provide_summary():
    """Provide summary and next steps."""
    print("\n" + "=" * 70)
    print("SUMMARY - Your Options Without Router Admin Access")
    print("=" * 70)
    print("""
Here's what you can do (in order of recommendation):

1. ✅ CHECK CONNECTED DEVICES
   → Phone (Android is easiest)
   → Other computers
   → Tablets
   → Use our tool: wifi_password_retriever.py

2. ✅ CHECK ROUTER LABEL
   → Look on bottom/back of router
   → Check original packaging
   → Find manual/setup card

3. ✅ CONTACT YOUR ISP
   → They can help if it's their router
   → May reset password remotely
   → Free technical support

4. ✅ ASK AROUND
   → Whoever set up the router
   → Check shared documents/passwords
   → Family members

5. ⚠️ ROUTER RESET (Last Resort)
   → Only if nothing else works
   → Requires full setup again
   → Consider ISP help first

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 NEXT STEPS:

   1. Start with easiest options first (phone, label)
   2. Use our automated tools when possible
   3. Don't reset router unless absolutely necessary
   4. Once recovered, save password securely!
   5. Generate QR code: python3 wifi_qr_generator.py

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")


def main():
    """Main function to guide user through WiFi recovery."""
    print("=" * 70)
    print("WiFi Password Recovery - No Router Admin Access")
    print("=" * 70)
    print("\nYou mentioned you don't have access to the router admin panel.")
    print("Don't worry! There are several other ways to recover your password.")
    print("\nLet's go through your options...\n")
    
    input("Press Enter to start...")
    
    # Method 1: Check phone
    has_phone = check_phone_connected()
    if has_phone:
        print("\n✓ Great! Try the phone method above.")
        print("  This is usually the easiest and fastest way!")
        response = input("\nDid you find the password? (y/n): ")
        if response.lower() in ['y', 'yes']:
            print("\n🎉 Excellent! You're all set!")
            print("\n💡 TIP: Run 'python3 wifi_qr_generator.py' to create a QR code")
            print("   for easy sharing in the future!")
            sys.exit(0)
    
    # Method 2: Router label
    can_check_router = check_router_label()
    if can_check_router:
        response = input("\nDid you find the password on the router? (y/n): ")
        if response.lower() in ['y', 'yes']:
            print("\n🎉 Perfect! Problem solved!")
            print("\n💡 TIP: If the password was hard to read or long,")
            print("   consider changing it to something easier using router admin.")
            sys.exit(0)
        else:
            print("\nThe label probably shows the DEFAULT password.")
            print("If someone changed it, the label won't match.")
    
    # Method 3: Other computers
    has_other_computers = check_other_computers()
    if has_other_computers:
        print("\n✓ Try running our tool on those computers!")
        print("  Windows: python wifi_password_retriever.py")
        print("  Linux: sudo python3 wifi_password_retriever.py")
        response = input("\nDid you retrieve the password? (y/n): ")
        if response.lower() in ['y', 'yes']:
            print("\n🎉 Success! You've recovered your password!")
            sys.exit(0)
    
    # Method 4: Contact ISP
    has_isp = contact_isp_info()
    if has_isp:
        print("\n✓ Contact your ISP - they're usually very helpful!")
        print("  This is often the quickest solution when other methods fail.")
        input("\nPress Enter to see remaining options...")
    
    # Method 5: Ask around
    check_ask_neighbors()
    
    # Method 6: Reset (last resort)
    print("\n" + "!" * 70)
    print("If none of the above methods worked, you have one last option...")
    print("!" * 70)
    
    wants_reset = router_reset_warning()
    if wants_reset:
        print("\n" + "⚠️" * 35)
        print("\nBefore proceeding with reset:")
        print("1. Save this guide for setup reference")
        print("2. Have ISP contact info ready")
        print("3. Warn all WiFi users")
        print("4. Consider calling ISP for remote help first")
        print("\nGood luck with the reset!")
        print("⚠️" * 35)
    else:
        print("\n✓ Good choice! Try contacting your ISP first.")
        print("  They can often help without needing a reset.")
    
    # Summary
    provide_summary()
    
    print("\nNeed more help? Check WIFI_RECOVERY_GUIDE.md for detailed instructions.")


if __name__ == "__main__":
    main()
