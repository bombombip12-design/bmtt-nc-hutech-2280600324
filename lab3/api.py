from flask import Flask, request, jsonify
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher

app = Flask(__name__)

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher()

# CAESAR CIPHER ALGORITHM
class CaesarCipher:
    def __init__(self):
        self.alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + key) % alphabet_len
                output_letter = self.alphabet[output_index]
                encrypted_text.append(output_letter)
            else:
                encrypted_text.append(letter)  # Giữ nguyên ký tự không phải chữ cái
        return "".join(encrypted_text)
    
    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index - key) % alphabet_len
                output_letter = self.alphabet[output_index]
                decrypted_text.append(output_letter)
            else:
                decrypted_text.append(letter)  # Giữ nguyên ký tự không phải chữ cái
        return "".join(decrypted_text)

caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    try:
        data = request.json
        plain_text = data['plain_text']
        key = int(data['key'])
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({"encrypted_message": encrypted_text})
    except ValueError:
        return jsonify({"error": "Invalid key. Key must be an integer."}), 400
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    try:
        data = request.json
        cipher_text = data['cipher_text']
        key = int(data['key'])
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({"decrypted_message": decrypted_text})
    except ValueError:
        return jsonify({"error": "Invalid key. Key must be an integer."}), 400
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({"message": "RSA keys generated successfully"})

@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    try:
        data = request.json
        message = data['message']
        key_type = data['key_type']
        private_key, public_key = rsa_cipher.load_keys()
        if key_type == 'public':
            key = public_key
        elif key_type == 'private':
            key = private_key
        else:
            return jsonify({"error": "Invalid key type"}), 400
        encrypted_message = rsa_cipher.encrypt(message, key)
        encrypted_hex = encrypted_message.hex()
        return jsonify({"encrypted_message": encrypted_hex})
    except FileNotFoundError:
        return jsonify({"error": "Keys not found. Please generate keys first."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    try:
        data = request.json
        ciphertext_hex = data['cipher_text']
        key_type = data['key_type']
        private_key, public_key = rsa_cipher.load_keys()
        if key_type == 'public':
            key = public_key
        elif key_type == 'private':
            key = private_key
        else:
            return jsonify({"error": "Invalid key type"}), 400
        cipher_text = bytes.fromhex(ciphertext_hex)
        decrypted_message = rsa_cipher.decrypt(cipher_text, key)
        # Decode bytes thành string
        try:
            decrypted_str = decrypted_message.decode('utf-8')
        except UnicodeDecodeError:
            return jsonify({"error": "Decryption failed: Invalid ciphertext or key"}), 400
        return jsonify({"decrypted_message": decrypted_str})
    except FileNotFoundError:
        return jsonify({"error": "Keys not found. Please generate keys first."}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign_message():
    try:
        data = request.json
        message = data['message']
        private_key, _ = rsa_cipher.load_keys()
        signature = rsa_cipher.sign(message, private_key)
        signature_hex = signature.hex()
        return jsonify({"signature": signature_hex})
    except FileNotFoundError:
        return jsonify({"error": "Keys not found. Please generate keys first."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify_signature():
    try:
        data = request.json
        message = data['message']
        signature_hex = data['signature']
        _, public_key = rsa_cipher.load_keys()
        signature = bytes.fromhex(signature_hex)
        is_verified = rsa_cipher.verify(message, signature, public_key)
        return jsonify({"is_valid": is_verified})
    except FileNotFoundError:
        return jsonify({"error": "Keys not found. Please generate keys first."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# ECC CIPHER ALGORITHM
ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
