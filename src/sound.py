import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Parameters
duration = 10  # seconds
sampling_rate = 140000 # samples per second

print("Recording...")

# Record audio
audio = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=1, dtype='float64')
sd.wait()

print("Recording complete.")

# Flatten the audio to 1D
audio = audio.flatten()

# Time axis
time = np.linspace(0, duration, len(audio))

plt.figure(figsize=(12, 4))
plt.plot(time, audio)
plt.title("Time Domain - Audio Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

write("recording.wav", sampling_rate, audio)
print("Saved as recording.wav")


n = len(audio)
audio_fft = np.fft.fft(audio)
frequencies = np.fft.fftfreq(n, d=1/sampling_rate)
magnitude = np.abs(audio_fft) / n

# Plot only positive frequencies
mask = frequencies >= 0
frequencies = frequencies[mask]
magnitude = magnitude[mask]

# Plot Frequency Domain
plt.figure(figsize=(12, 4))
plt.plot(frequencies, magnitude)
plt.title("Frequency Domain - Magnitude Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.show()