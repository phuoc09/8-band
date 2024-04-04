def binary_array_to_decimal(array):
    # Khởi tạo một mảng mới để lưu trữ giá trị thập phân
    decimal_array = []
    # Duyệt qua mỗi phần tử trong mảng nhị phân
    for binary_str in array:
        # Kiểm tra bit dấu
        if binary_str[0] == '1':
            # Trường hợp số âm: áp dụng biểu diễn bù hai
            # Đảo bit (bitwise NOT)
            complement = ''.join('1' if bit == '0' else '0' for bit in binary_str)
            # Chuyển thành số nguyên và cộng 1
            decimal = -(int(complement, 2) + 1)
        else:
            # Trường hợp số dương: chuyển trực tiếp sang số nguyên
            decimal = int(binary_str, 2)
        # Thêm giá trị thập phân vào mảng mới
        decimal_array.append(decimal)
    return decimal_array

import numpy as np
from scipy.io.wavfile import write

# Đọc tệp văn bản chứa các giá trị âm lượng nhị phân
amplitude_values_binary = np.loadtxt('amplitude_values.txt', dtype=str)

# Chuyển đổi các giá trị nhị phân sang số nguyên thập phân
amplitude_values_decimal = binary_array_to_decimal(amplitude_values_binary)

# Chuyển danh sách các giá trị âm lượng thành mảng numpy
audio_data = np.array(amplitude_values_decimal, dtype=np.int16)

# Ghi dữ liệu âm thanh vào tệp WAV
write('renew.wav', 16000, audio_data)