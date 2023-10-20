import pyaudio
import wave
import time

def record_audio(output_file):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    frames = []

    try:
        print("Recording...")
        start_time = time.time()

        while time.time() - start_time < 4:
            data = stream.read(1024)
            frames.append(data)
    except KeyboardInterrupt:
        print("Recording stopped.")
        pass

    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(output_file, "wb")
    waveFile.setnchannels(1)
    waveFile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
    waveFile.setframerate(16000)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

if __name__ == "__main__":
    record_audio("output.wav")  