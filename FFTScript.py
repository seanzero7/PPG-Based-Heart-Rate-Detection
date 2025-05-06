import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("CSVs/Logan.csv")

t = df["t_sec"].values
brightness = df["brightness"].values

# Compute FFT
dt = t[1] - t[0]
N = len(brightness)

fft_vals = np.fft.fft(brightness)
freqs = np.fft.fftfreq(N, dt)

# Only positive frequencies
pos_mask = freqs > 0
fft_vals = fft_vals[pos_mask]
freqs = freqs[pos_mask]

# Only 0–3 Hz
freq_mask = (freqs >= 0) & (freqs <= 3)
freqs = freqs[freq_mask]
fft_vals = fft_vals[freq_mask]

# Find peak frequency
peak_idx = np.argmax(np.abs(fft_vals))
peak_freq = freqs[peak_idx]
peak_amp = np.abs(fft_vals[peak_idx])
heart_rate_bpm = peak_freq * 60

# Plot
plt.figure(figsize=(10, 5))
plt.plot(freqs, np.abs(fft_vals), linewidth=1)
plt.axvline(peak_freq, color='red', linestyle='--', label=f'Peak: {peak_freq:.2f} Hz\n({heart_rate_bpm:.0f} bpm)')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT of Brightness Signal (0–3 Hz)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print(f"Estimated heart rate: {heart_rate_bpm:.1f} bpm")
