## 🚀 CryptDir_Pro

CryptDir_Pro is a lightweight Python tool that allows you to encrypt and decrypt the contents of all files within a directory using the Fernet symmetric encryption algorithm. The tool ensures that the contents of files are secured, while leaving the directory structure intact.

## 🔒 Features
- Encrypt/Decrypt File Contents: Secure the contents of all files in a directory.
- Password-Protected: Uses a password-based key derivation function (PBKDF2).
- Symmetric Encryption: Leverages the Fernet encryption scheme, based on AES-128 in CBC mode.
- Interactive Menu: Provides a clean, interactive CLI experience.
- Keeps the file system structure intact and just encrypts content of files present in the Directory

## 🛠️ Usage:

# Installation: 
- Clone the repository:
git clone https://github.com/yourusername/CryptDir_Pro.git
- cd CryptDir_Pro

# Install dependencies:
- pip install -r requirements.txt
- You don't need to add os, base64, getpass, and pathlib to requirements.txt because they are part of Python's standard library and are automatically included with Python installations. The requirements.txt file is specifically for third-party libraries (such as cryptography and pyfiglet) that need to be installed separately.

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

# Supported File Types 📂
CryptDir_Pro can encrypt the contents of various file types, including but not limited to:

- Text files: .txt, .md, .csv, .log
- Documents: .pdf, .docx, .pptx, .xlsx
- Images: .jpeg, .jpg, .png, .gif, .bmp
- Videos: .mp4, .mkv, .avi
- Audio: .mp3, .wav, .flac
- Code files: .py, .java, .js, .html, .css, .php, .cpp
- Archives: .zip, .rar, .tar, .gz
- Executables: .exe, .bin, .dll
- Configuration files: .json, .yaml, .ini, .xml
  
Essentially, CryptDir_Pro can encrypt the contents of any file type regardless of the format.

# 📄 License
This project is licensed under the GPL License. See the LICENSE file for details.

# 👨‍💻 Author
coldman07
Feel free to contribute, report issues, or fork the project!
