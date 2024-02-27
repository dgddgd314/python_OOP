class CaesarCipherSolver:
    def __init__(self, shift):
        self.shift = shift

    def solve(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                decrypted_char = chr((ord(char) - ascii_offset - self.shift) % 26 + ascii_offset)
                plaintext += decrypted_char
            else:
                plaintext += char
        return plaintext

# 예제 사용법
shift_value = 3  # 예시로 3글자씩 이동한다고 가정
cipher_solver = CaesarCipherSolver(shift_value)

# 암호문
encrypted_text = "L fdhvdu fkduud, p wklv lv d whvw phvvdjh."

# 암호 해독
decrypted_text = cipher_solver.solve(encrypted_text)

print(f"암호문: {encrypted_text}")
print(f"해독된 문장: {decrypted_text}")
