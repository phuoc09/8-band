import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, lfilter
def fir_lpf(file_in,file_out,cutoff,order):
# Đọc tệp âm thanh đầu vào
    sample_rate, input_data = wavfile.read(file_in)

# Thiết lập thông số của bộ lọc
    nyquist_rate = 0.5 * sample_rate  # Tần số Nyquist

    cutoff_freq = cutoff  # Tần số cắt (Hz)
    if cutoff_freq >= nyquist_rate:
        raise ValueError("Invalid cutoff frequency: cutoff frequency must be less than Nyquist frequency (fs/2)")

    filter_order = order   # Bậc của bộ lọc

# Tạo hệ số của bộ lọc FIR bằng hàm firwin
    filter_coefficients = firwin(filter_order, cutoff_freq/nyquist_rate)

# Áp dụng bộ lọc FIR vào tín hiệu âm thanh
    filtered_output = lfilter(filter_coefficients, 1, input_data)
# luu file
    wavfile.write(file_out, sample_rate, np.asarray(filtered_output, dtype=np.int16))
