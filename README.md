# msound
Library for sound generation with math operations.
## Supported operations
- Sine wave (msin function)
- Sweep (msweep function)
- Noise (mnoise function)
## Examples

Sine wave sound generate:
```python
from msound.msin import msin

msin(freq=200, duration=1.2, filename="low.wav") # Low sound

msin(freq=1200, duration=1.2, filename="high.wav") # High sound
```

Sweep sound generate:
```python
from msound.msweep import msweep

msweep(200, 1500, 10.0, "sweep.wav") # 200 - start freq, 1500 - end freq, 10.0 - duration
```

Noise sound generate:
```python
from msound.mnoise import mnoise

mnoise(1.5, "noise.wav")
```

## Pages
PyPI: https://pypi.org/project/msound

GitHub: https://github.com/mistertay0dimon/msound
