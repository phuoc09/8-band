def decimal_to_signed_binary(decimal):
    if decimal >= 0:
        # Chuyển đổi số dương thành nhị phân
        binary = bin(decimal)[2:]
        # Điền các bit 0 phía trước nếu cần thiết để có độ dài 16 bit
        binary = binary.zfill(16)
    else:
        # Chuyển đổi số âm thành nhị phân bằng cách sử dụng 2's complement
        # Tính giá trị tuyệt đối của số âm
        abs_decimal = abs(decimal+1)
        # Chuyển đổi giá trị tuyệt đối sang nhị phân
        binary = bin(abs_decimal)[2:]
        # Điền các bit 0 phía trước nếu cần thiết để có độ dài 15 bit
        binary = binary.zfill(15)
        # Thực hiện phép đảo bit
        binary = ''.join('1' if bit == '0' else '0' for bit in binary)
        # Thêm bit 1 đầu tiên để biểu diễn số âm
        binary = '1' + binary
    return binary


import numpy as np
from scipy.io import wavfile

# Đọc tệp âm thanh WAV
sample_rate, audio_data = wavfile.read('pi.wav')
print(sample_rate)
# Lưu các giá trị biên độ vào tệp văn bản
with open('amplitude_values.txt', 'w') as file:
    for amplitude in audio_data:
        amplitude=decimal_to_signed_binary(amplitude)
        file.write(f"{amplitude}\n")
