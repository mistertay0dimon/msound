import numpy as np
from .writer import save_wav

def msweep(freq_start, freq_end, duration=1.0, filename="sweep.wav", sample_rate=44100, volume=0.5):
    """
    Generate sound with varying frequency.
    """

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # linear frequency change
    freqs = np.linspace(freq_start, freq_end, len(t))

    wave = volume * np.sin(2 * np.pi * freqs * t)

    save_wav(filename, wave, sample_rate)
    return filename