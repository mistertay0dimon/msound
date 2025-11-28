import wave
import numpy as np

def save_wav(filename, data, sample_rate=44100):
    audio = (data * 32767).astype(np.int16)

    with wave.open(filename, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())
