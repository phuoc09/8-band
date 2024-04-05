import os
import wave
import numpy as np

def add_amplitude(folder_path, output_file):
    # Tính tổng biên độ của tất cả các tệp WAV trong thư mục
    total_amplitude = None
    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            filepath = os.path.join(folder_path, filename)
            with wave.open(filepath, 'rb') as wav_file:
                # Đọc dữ liệu âm thanh
                params = wav_file.getparams()
                frames = wav_file.readframes(params.nframes)
                current_amplitude = np.frombuffer(frames, dtype=np.int16)
                
                # Thêm vào tổng biên độ
                if total_amplitude is None:
                    total_amplitude = np.copy(current_amplitude)
                else:
                    total_amplitude += current_amplitude

    # Ghi dữ liệu âm thanh mới
    if total_amplitude is not None:
        with wave.open(output_file, 'wb') as output_wav:
            output_wav.setparams(params)
            output_wav.writeframes(total_amplitude.tobytes())


