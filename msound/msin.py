import numpy as np
from .writer import save_wav

def msin(freq=440, duration=1.0, filename="output.wav", sample_rate=44100, volume=0.5):
    """
    Generate simple sinosouadle sound and saving to WAV file.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = volume * np.sin(2 * np.pi * freq * t)

    save_wav(filename, wave, sample_rate)
    return filename
