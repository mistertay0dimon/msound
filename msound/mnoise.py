import numpy as np
from .writer import save_wav

def mnoise(duration=1.0, filename="noise.wav", sample_rate=44100, volume=0.5):
    """
    Generating a file with noise.
    """
    length = int(sample_rate * duration)

    # uniform white noise
    wave = volume * (np.random.rand(length) * 2.0 - 1.0)

    save_wav(filename, wave, sample_rate)
    return filename