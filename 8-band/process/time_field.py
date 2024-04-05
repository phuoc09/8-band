import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
def print_time(file_in):
    sample_rate, input_data = wavfile.read(file_in)
    time = np.arange(len(input_data)) / sample_rate
# Vẽ biểu đồ biên độ theo thời gian
    plt.figure(figsize=(10, 6))
    plt.plot(time, input_data, label='Signal', alpha=0.7)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('WAV in time filed')
    plt.legend()
    plt.grid(True)
    plt.show()
