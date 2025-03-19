## 🚀 CryptDir_Pro

CryptDir_Pro is a lightweight Python tool that allows you to encrypt and decrypt the contents of all files within a directory using the Fernet symmetric encryption algorithm. The tool ensures that the contents of files are secured, while leaving the directory structure intact.

## 🔒 Features
- Encrypt/Decrypt File Contents: Secure the contents of all files in a directory.
- Password-Protected: Uses a password-based key derivation function (PBKDF2).
- Symmetric Encryption: Leverages the Fernet encryption scheme, based on AES-128 in CBC mode.
- Interactive Menu: Provides a clean, interactive CLI experience.
  
## 🛠️ Usage

# Installation: 
- Clone the repository:
git clone https://github.com/yourusername/CryptDir_Pro.git
cd CryptDir_Pro

# Install dependencies:
- pip install -r requirements.txt

# Running the Tool
To start the encryption/decryption process:
 python cryptdir_pro.py
- The program will prompt for a password (which is used to derive an encryption key).
- Choose between encryption or decryption.
- Enter the directory path that contains the files to process.
- The tool will only encrypt the contents of files, not the directory itself.

# 🧑‍💻 Example

-> Enter encryption/decryption key: ********

-> Do you want to encrypt or decrypt the directory? (encrypt/decrypt): encrypt

-> Enter the full path of the directory to be encrypted/decrypted: /path/to/directory

-> After this, all files inside the directory will be encrypted/decrypted, and the changes will be reflected in the original files.

# 🔑 Encryption/Decryption
The tool uses a password-based key derivation function (PBKDF2) with SHA256 and a static salt (for demo purposes). Ensure that the password is securely stored.

📄 License
This project is licensed under the GPL License. See the LICENSE file for details.

👨‍💻 Author
coldman07
Feel free to contribute, report issues, or fork the project!
Feel free to customize this further for your repository!
