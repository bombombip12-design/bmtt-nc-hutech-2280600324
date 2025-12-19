import sys
import os
import rsa

# GUI imports - only needed when running as script
GUI_AVAILABLE = False
try:
    # Only import GUI when running directly, not when imported as module
    if __name__ == "__main__":
        # Add parent directories to path for GUI imports
        import pathlib
        lab3_dir = pathlib.Path(__file__).parent.parent.parent
        sys.path.insert(0, str(lab3_dir))
        
        from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
        from ui.rsa import Ui_MainWindow
        import requests
        GUI_AVAILABLE = True
except ImportError:
    pass

if GUI_AVAILABLE:
    class MyApp(QMainWindow):
        """GUI Application class for RSA Cipher."""
        def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.call_api_gen_keys)
            self.ui.pushButton_2.clicked.connect(self.call_api_encrypt)
            self.ui.pushButton_3.clicked.connect(self.call_api_decrypt)
            self.ui.pushButton_4.clicked.connect(self.call_api_sign)
            self.ui.pushButton_5.clicked.connect(self.call_api_verify)
        
        def call_api_gen_keys(self):
            url = "http://127.0.0.1:5000/api/rsa/generate_keys"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Keys Generated Successfully")
                    msg.exec_()
                else:
                    print("Error while calling API")
            except requests.exceptions.RequestException as e:
                print("Error: %s" % str(e))
    
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.textEdit.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_2.setText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))
    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.textEdit_2.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setText(data["decrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))
    
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.textEdit_3.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_4.setText(data["signature"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))
    
    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.textEdit_3.toPlainText(),
            "signature": self.ui.textEdit_4.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data.get("is_valid", False) or data.get("is_verified", False):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Verification Failed")
                    msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))
else:
    class MyApp:
        """GUI Application class for RSA Cipher. GUI not available."""
        def __init__(self):
            raise RuntimeError("GUI dependencies not available. Run this file directly, not as a module.")

class RSACipher:
    def __init__(self):
        self.keys_dir = os.path.join(os.path.dirname(__file__), 'keys')
        self.private_key_path = os.path.join(self.keys_dir, 'private_key.pem')
        self.public_key_path = os.path.join(self.keys_dir, 'public_key.pem')
        
    def load_keys(self):
        """Load RSA keys from files, or generate new ones if they don't exist."""
        if not os.path.exists(self.private_key_path) or not os.path.exists(self.public_key_path):
            # Generate new keys if they don't exist
            self._generate_keys()
        
        # Load keys from files
        with open(self.private_key_path, 'rb') as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
        
        with open(self.public_key_path, 'rb') as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
        
        return private_key, public_key
    
    def generate_keys(self):
        """Generate new RSA key pair and save them to files."""
        self._generate_keys()
    
    def _generate_keys(self):
        """Generate new RSA key pair and save them to files."""
        # Ensure keys directory exists
        os.makedirs(self.keys_dir, exist_ok=True)
        
        # Generate key pair (2048-bit keys)
        (public_key, private_key) = rsa.newkeys(2048)
        
        # Save private key
        with open(self.private_key_path, 'wb') as f:
            f.write(private_key.save_pkcs1())
        
        # Save public key
        with open(self.public_key_path, 'wb') as f:
            f.write(public_key.save_pkcs1())
    
    def encrypt(self, message, key):
        """Encrypt a message with an RSA key.
        
        Args:
            message: String message to encrypt
            key: RSA public key or private key
            
        Returns:
            bytes: Encrypted message
        """
        message_bytes = message.encode('utf-8')
        encrypted = rsa.encrypt(message_bytes, key)
        return encrypted
    
    def decrypt(self, ciphertext, key):
        """Decrypt ciphertext with an RSA key.
        
        Args:
            ciphertext: Bytes ciphertext to decrypt
            key: RSA private key (for decryption)
            
        Returns:
            str: Decrypted message
        """
        decrypted_bytes = rsa.decrypt(ciphertext, key)
        return decrypted_bytes.decode('utf-8')
    
    def sign(self, message, private_key):
        """Sign a message with a private key.
        
        Args:
            message: String message to sign
            private_key: RSA private key
            
        Returns:
            bytes: Signature
        """
        message_bytes = message.encode('utf-8')
        signature = rsa.sign(message_bytes, private_key, 'SHA-256')
        return signature
    
    def verify(self, message, signature, public_key):
        """Verify a signature with a public key.
        
        Args:
            message: String message that was signed
            signature: Bytes signature to verify
            public_key: RSA public key
            
        Returns:
            bool: True if signature is valid, False otherwise
        """
        try:
            message_bytes = message.encode('utf-8')
            rsa.verify(message_bytes, signature, public_key)
            return True
        except rsa.VerificationError:
            return False

if __name__ == "__main__":
    if not GUI_AVAILABLE:
        print("Error: GUI dependencies not available. Please install PyQt5 and ensure ui.rsa module exists.")
        sys.exit(1)
    
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
