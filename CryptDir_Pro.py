import os
import base64
import getpass
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from pathlib import Path
import pyfiglet 


def print_banner():
    ascii_art = pyfiglet.figlet_format("CryptDir_Pro")  # Generate the ASCII art
    creator_credit = "Created by coldman07"  # Add creator credit
    print(ascii_art)
    print(creator_credit)
    print("Directory Encryption/Decryption Tool\n")
# Function to generate a key from a password
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),  # Use the correct algorithm object
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
# Function to encrypt a file
def encrypt_file(file_path, fernet):
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
        encrypted_data = fernet.encrypt(file_data)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        print(f"Encrypted: {file_path}")
    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")
# Function to decrypt a file
def decrypt_file(file_path, fernet):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(file_path, 'wb') as f:
            f.write(decrypted_data)
        print(f"Decrypted: {file_path}")
    except Exception as e:
        print(f"Error decrypting {file_path}: {e}")
# Function to process a directory for encryption or decryption
def process_directory(directory_path, fernet, operation):
    for root, _, files in os.walk(directory_path):
        for file in files:
            # Skip encrypting the script itself
            if file == os.path.basename(__file__):
                continue
            file_path = os.path.join(root, file)
            if operation == 'encrypt':
                encrypt_file(file_path, fernet)
            elif operation == 'decrypt':
                decrypt_file(file_path, fernet)
def main():
    print_banner()  # Display CryptDir Pro banner
    # Use a fixed salt for demonstration purposes (in production, store the salt securely)
    salt = b'\x00\x01\x02\x03\x04\x05\x06\x07'
    # Main loop to keep the menu running
    while True:
        # Get the password from the user
        password = getpass.getpass("Enter encryption/decryption key: ")
        # Generate key using PBKDF2
        key = generate_key(password, salt)
        fernet = Fernet(key)
        # Ask for operation (encrypt or decrypt)
        while True:
            operation = input("Do you want to encrypt or decrypt the directory? (encrypt/decrypt): ").strip().lower()
            if operation in ['encrypt', 'decrypt']:
                break
            print("Invalid option. Please enter 'encrypt' or 'decrypt'.")
        # Get the directory path from the user
        directory_path = input("Enter the full path of the directory to be encrypted/decrypted: ").strip()
        # Ensure the directory exists
        if not os.path.isdir(directory_path):
            print("The specified directory does not exist.")
            continue
        # Confirmation step
        confirm = input(f"This will {operation} all files in {directory_path}. Continue? (y/n): ").strip().lower()
        if confirm != 'y':
            print(f"{operation.capitalize()} operation cancelled.")
            continue
        # Perform encryption or decryption
        print(f"Starting {operation}ion of directory: {directory_path}")
        process_directory(directory_path, fernet, operation)
        print(f"{operation.capitalize()}ion complete.")
        # Ask if the user wants to perform another operation
        again = input("Do you want to perform another operation? (y/n): ").strip().lower()
        if again != 'y':
            print("Exiting the tool. Goodbye!")
            break
if __name__ == "__main__":
    main()
