import numpy as np
from scipy.io import wavfile
def decimal_to_signed_binary(decimal):
    if decimal >= 0:
        # Chuyển đổi số dương thành nhị phân
        binary = bin(decimal)[2:]
        # Điền các bit 0 phía trước nếu cần thiết để có độ dài 16 bit
        binary = binary.zfill(16)
    else :
        # Chuyển đổi số dương thành nhị phân
        binary = bin(-decimal)[2:]
        # Điền các bit 0 phía trước nếu cần thiết để có độ dài 16 bit
        binary = binary.zfill(15)
        binary = '1'+ binary  
    return binary
def Read(file_in,file_out):
    # Đọc tệp âm thanh WAV
    sample_rate, audio_data = wavfile.read(file_in)
    # Lưu các giá trị biên độ vào tệp văn bản
    with open(file_out, 'w') as file:
        for amplitude in audio_data:
            amplitude=decimal_to_signed_binary(amplitude)
            file.write(f"{amplitude}\n")



