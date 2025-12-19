class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        
        # Lặp qua từng cột (với 'key' là số cột)
        for col in range(key):
            pointer = col
            
            # Đọc xuống dưới từng cột
            while pointer < len(text):
                encrypted_text += text[pointer]
                # Chuyển đến hàng tiếp theo (cùng cột)
                pointer += key
                
        return encrypted_text

    def decrypt(self, text, key):
        # Khởi tạo danh sách cho văn bản đã giải mã, với độ dài bằng 'key'
        # Mỗi phần tử là một chuỗi rỗng đại diện cho một cột trong ma trận giải mã.
        # Lưu ý: 'key' là số cột, không phải độ dài của văn bản đã giải mã
        # Dựa trên code trong ảnh: decrypted_text = [''] * key
        decrypted_text = [''] * key 
        
        row, col = 0, 0
        
        # Điền các ký tự của ciphertext vào các "cột"
        for symbol in text:
            # Thêm ký tự vào cột hiện tại
            decrypted_text[col] += symbol
            col += 1
            
            # Điều kiện xuống dòng trong ma trận giải mã:
            # 1. Khi đã điền đầy đủ các cột (col == key)
            # HOẶC
            # 2. Khi ở cột cuối cùng (col == key - 1) VÀ đã điền hết các hàng có ký tự
            # (row >= len(text) % key)
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1

        # Nối các cột (là các hàng trong ma trận giải mã) lại với nhau
        return "".join(decrypted_text)