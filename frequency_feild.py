import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Đọc tệp âm thanh
sample_rate, data = wavfile.read('./bpf.wav')

# Thực hiện FFT để chuyển đổi dữ liệu sang miền tần số
fft_output = np.fft.fft(data)

# Tính toán các tần số tương ứng với các điểm dữ liệu
freqs = np.fft.fftfreq(len(fft_output), 1/sample_rate)

# Loại bỏ nửa phổ không cần thiết (do đối xứng)
half_length = len(freqs)//2
freqs = freqs[:half_length]
fft_output = fft_output[:half_length]

# Vẽ biểu đồ phổ tần số
plt.figure(figsize=(10, 6))
plt.plot(freqs, np.abs(fft_output))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
plt.grid(True)
plt.show()
