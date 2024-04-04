import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, lfilter

# Đọc tệp âm thanh đầu vào
sample_rate, input_data = wavfile.read('pi.wav')

# Thiết lập thông số của bộ lọc
nyquist_rate = 0.5 * sample_rate  # Tần số Nyquist
low_cutoff_freq = 1000  # Tần số cắt dưới (Hz)
high_cutoff_freq = 4000  # Tần số cắt trên (Hz)

if low_cutoff_freq >= high_cutoff_freq or high_cutoff_freq >= nyquist_rate:
    raise ValueError("Invalid cutoff frequencies: The high cutoff frequency must be lower than Nyquist frequency "
                     "and higher than the low cutoff frequency.")

filter_order = 500   # Bậc của bộ lọc

# Tạo hệ số của bộ lọc thông dải FIR bằng hàm firwin
filter_coefficients = firwin(filter_order + 1, [low_cutoff_freq/nyquist_rate, high_cutoff_freq/nyquist_rate], pass_zero=False)

# Áp dụng bộ lọc thông dải FIR vào tín hiệu âm thanh
filtered_output = lfilter(filter_coefficients, 1, input_data)

# Lưu tín hiệu âm thanh đã lọc vào tệp mới
wavfile.write('bpf.wav', sample_rate, np.asarray(filtered_output, dtype=np.int16))

# Vẽ biểu đồ so sánh tín hiệu âm thanh gốc và tín hiệu đã lọc
plt.figure(figsize=(10, 6))
plt.plot(input_data, label='Original Signal', alpha=0.7)
plt.plot(filtered_output, label='Filtered Signal', alpha=0.7)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Comparison of Original and Band-pass Filtered Signals')
plt.legend()
plt.grid(True)
plt.show()