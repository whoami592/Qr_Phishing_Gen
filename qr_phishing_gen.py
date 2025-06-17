import qrcode
from datetime import datetime

# Stylish ASCII banner
def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════╗
    ║         QR Code Phishing Generator                 ║
    ║   Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan ║
    ║         Created on: {}         ║
    ╚════════════════════════════════════════════════════╝
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(banner)

# Function to generate QR code
def generate_qr_code(url, filename="phishing_qr.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data (URL) to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

def main():
    # Print the banner
    print_banner()
    
    # Get URL from user (default is a placeholder phishing URL)
    url = input("Enter the phishing URL (e.g., http://fake-login.com): ") or "http://fake-login.com"
    
    # Generate QR code
    generate_qr_code(url)
    
    print("\nNote: This tool is for educational purposes only. Use ethically and responsibly.")

if __name__ == "__main__":
    main()