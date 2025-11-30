import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Parameters
duration = 30 
sampling_rate = 140000  

print("Recording...")

audio = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=2, dtype='float64')
sd.wait()

print("Recording complete.")

# Time axis for time-domain plot
time = np.linspace(0, duration, audio.shape[0])
# Convert float audio to int16 for saving
max_val = np.max(np.abs(audio))
audio_int16 = np.int16(audio / max_val * 32767)
write("recording.wav", sampling_rate, audio_int16)

print("Saved as recording.wav")

# Plot time-domain signal
plt.figure(figsize=(12, 4))
plt.plot(time, audio)
plt.title("Time Domain - Audio Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()



# FFT for frequency-domain analysis
n = len(audio)
audio_fft = np.fft.fft(audio)
frequencies = np.fft.fftfreq(n, d=1/sampling_rate)
magnitude = np.abs(audio_fft) / n

# Only positive frequencies
mask = frequencies >= 0
frequencies = frequencies[mask]
magnitude = magnitude[mask]

# Plot frequency-domain signal
plt.figure(figsize=(12, 4))
plt.plot(frequencies, magnitude)
plt.title("Frequency Domain - Magnitude Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()
