import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, lfilter
def fir_bpf(file_in,file_out,low_cut,high_cut,order):
# Đọc tệp âm thanh đầu vào
    sample_rate, input_data = wavfile.read(file_in)

# Thiết lập thông số của bộ lọc
    nyquist_rate = 0.5 * sample_rate  # Tần số Nyquist
    low_cutoff_freq = low_cut  # Tần số cắt dưới (Hz)
    high_cutoff_freq = high_cut  # Tần số cắt trên (Hz)

    if low_cutoff_freq >= high_cutoff_freq or high_cutoff_freq >= nyquist_rate:
        raise ValueError("Invalid cutoff frequencies: The high cutoff frequency must be lower than Nyquist frequency "
                     "and higher than the low cutoff frequency.")

    filter_order = order   # Bậc của bộ lọc

# Tạo hệ số của bộ lọc thông dải FIR bằng hàm firwin
    filter_coefficients = firwin(filter_order + 1, [low_cutoff_freq/nyquist_rate, high_cutoff_freq/nyquist_rate], pass_zero=False)

# Áp dụng bộ lọc thông dải FIR vào tín hiệu âm thanh
    filtered_output = lfilter(filter_coefficients, 1, input_data)

# Lưu tín hiệu âm thanh đã lọc vào tệp mới
    wavfile.write(file_out, sample_rate, np.asarray(filtered_output, dtype=np.int16))

