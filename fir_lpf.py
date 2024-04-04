import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import firwin, lfilter

# Đọc tệp âm thanh đầu vào
sample_rate, input_data = wavfile.read('pi.wav')

# Thiết lập thông số của bộ lọc
nyquist_rate = 0.5 * sample_rate  # Tần số Nyquist

cutoff_freq = 1000  # Tần số cắt (Hz)
if cutoff_freq >= nyquist_rate:
    raise ValueError("Invalid cutoff frequency: cutoff frequency must be less than Nyquist frequency (fs/2)")

filter_order = 100   # Bậc của bộ lọc

# Tạo hệ số của bộ lọc FIR bằng hàm firwin
filter_coefficients = firwin(filter_order, cutoff_freq/nyquist_rate)

# Áp dụng bộ lọc FIR vào tín hiệu âm thanh
filtered_output = lfilter(filter_coefficients, 1, input_data)

# Lưu tín hiệu âm thanh đã lọc vào tệp mới
wavfile.write('lpf.wav', sample_rate, np.asarray(filtered_output, dtype=np.int16))

# Vẽ biểu đồ so sánh tín hiệu âm thanh gốc và tín hiệu đã lọc
plt.figure(figsize=(10, 6))
plt.plot(input_data, label='Original Signal', alpha=0.7)
plt.plot(filtered_output, label='Filtered Signal', alpha=0.7)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Comparison of Original and Filtered Signals')
plt.legend()
plt.grid(True)
plt.show()