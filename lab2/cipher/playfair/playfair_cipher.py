class PlayFairCipher:
    def __init__(self):
        pass

    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        # Chuyển "J" thành "I" trong khóa
        key = key.replace("J", "I")
        key = key.upper()
        
        # Lấy các chữ cái duy nhất từ khóa để tạo key_set
        key_set = set(key)
        
        # Bảng chữ cái 25 ký tự (I và J được coi là 1)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # Tìm các chữ cái còn lại không có trong khóa
        remaining_letters = [
            letter for letter in alphabet if letter not in key_set
        ]
        
        # Khởi tạo ma trận (dưới dạng danh sách phẳng ban đầu)
        matrix = list(key)
        
        # Thêm các chữ cái còn lại
        for letter in remaining_letters:
            matrix.append(letter)
            # Ngừng khi ma trận đạt 25 ký tự
            if len(matrix) == 25:
                break
        
        # Chuyển đổi danh sách phẳng thành ma trận 5x5
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        # Tìm tọa độ (hàng, cột) của một chữ cái trong ma trận
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        # Trả về None nếu không tìm thấy (mặc dù không nên xảy ra)
        return None, None 

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        
        # Loại bỏ khoảng trắng và ký tự không phải chữ cái
        # (Không có trong ảnh, nhưng cần thiết cho Playfair thực tế. Giữ nguyên theo ảnh)
        # plain_text = "".join(filter(str.isalpha, plain_text)) 
        
        encrypted_text = ""

        # Lặp qua văn bản rõ ràng theo cặp (bigrams)
        # Lưu ý: Việc xử lý trùng lặp và padding 'X' cần được thực hiện trước vòng lặp này trong thực tế.
        # Đoạn code trong ảnh chỉ xử lý padding cuối cùng nếu độ dài là lẻ.
        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            
            # Xử lý nếu số lượng ký tự là lẻ
            if len(pair) == 1:
                pair += "X"

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            # Quy tắc 1: Cùng hàng (Row Rule)
            if row1 == row2:
                # Chuyển sang phải 1 vị trí (modulo 5)
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            
            # Quy tắc 2: Cùng cột (Column Rule)
            elif col1 == col2:
                # Chuyển xuống dưới 1 vị trí (modulo 5)
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]

            # Quy tắc 3: Hình chữ nhật (Rectangle Rule)
            else:
                # Trao đổi vị trí cột
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Ở đây cần có thêm logic để loại bỏ các cặp trùng lặp (ví dụ: 'AA' -> 'AX A')
        # và nối chuỗi đã xử lý (nếu có). Logic này không có trong ảnh của bạn.
        
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        # Lặp qua văn bản mã hóa theo cặp
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            # Quy tắc 1: Cùng hàng (Row Rule - ngược lại)
            if row1 == row2:
                # Chuyển sang trái 1 vị trí (modulo 5)
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            
            # Quy tắc 2: Cùng cột (Column Rule - ngược lại)
            elif col1 == col2:
                # Chuyển lên trên 1 vị trí (modulo 5)
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]

            # Quy tắc 3: Hình chữ nhật (Rectangle Rule - giống như mã hóa)
            else:
                # Trao đổi vị trí cột
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        banro = ""

        for i in range(0, len(decrypted_text) - 2, 2):
            if decrypted_text[i] == decrypted_text[i+2]:
                banro += decrypted_text[i]
            else:
                banro += decrypted_text[i] + "" + decrypted_text[i+1] # "" không tạo khoảng trắng

        if decrypted_text[-1] == "X":
            banro += decrypted_text[-2]
        else:
            banro += decrypted_text[-2]
            banro += decrypted_text[-1]
            
        return banro