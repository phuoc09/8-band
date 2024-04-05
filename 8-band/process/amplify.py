import numpy as np
import wave

def amplify_wav(input_file, output_file, amplification_factor_dB):
    # Mở tập tin WAV đầu vào
    with wave.open(input_file, 'rb') as wave_file:
        # Lấy thông tin từ tập tin WAV
        params = wave_file.getparams()
        num_frames = params.nframes
        sample_width = params.sampwidth
        num_channels = params.nchannels
        frame_rate = params.framerate

        # Đọc dữ liệu âm thanh
        frames = wave_file.readframes(num_frames)

    # Chuyển đổi dữ liệu âm thanh thành mảng numpy
    samples = np.frombuffer(frames, dtype=np.int16)

    # Tính toán hệ số để tăng biên độ
    amplification_factor = 10 ** (amplification_factor_dB / 20.0)

    # Tăng biên độ của mẫu âm thanh
    amplified_samples = samples * amplification_factor

    # Chuyển đổi lại sang kiểu dữ liệu int16
    amplified_samples = amplified_samples.astype(np.int16)

    # Ghi dữ liệu âm thanh đã được tăng biên độ vào tập tin WAV đầu ra
    with wave.open(output_file, 'wb') as output_wave_file:
        output_wave_file.setparams(params)
        output_wave_file.writeframes(amplified_samples.tobytes())

