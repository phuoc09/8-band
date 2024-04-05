import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, lfilter
def fir_hpf(file_in,file_out,cut_off,order):
# Đọc tệp âm thanh đầu vào
    sample_rate, input_data = wavfile.read(file_in)

# Thiết lập thông số của bộ lọc
    nyquist_rate = 0.5 * sample_rate  # Tần số Nyquist
    cutoff_freq = cut_off  # Tần số cắt (Hz) - ở đây là tần số cắt của bộ lọc thông cao
    if cutoff_freq >= nyquist_rate:
        cutoff_freq = 0.95 * nyquist_rate  # Đảm bảo tần số cắt nhỏ hơn tần số Nyquist

    filter_order = order   # Bậc của bộ lọc

# Tạo hệ số của bộ lọc thông cao FIR bằng hàm firwin
    filter_coefficients = firwin(filter_order + 1, cutoff_freq/nyquist_rate, pass_zero=False)

# Áp dụng bộ lọc thông cao FIR vào tín hiệu âm thanh
    filtered_output = lfilter(filter_coefficients, 1, input_data)

# Lưu tín hiệu âm thanh đã lọc vào tệp mới
    wavfile.write(file_out, sample_rate, np.asarray(filtered_output, dtype=np.int16))
