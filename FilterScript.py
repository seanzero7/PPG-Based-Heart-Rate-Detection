import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

csv_file = "CSVs/Logan.csv"  # CSV here
low_bpm = 40.0
high_bpm = 180.0

# Load CSV 
df = pd.read_csv(csv_file)
t = df["t_sec"].values
brightness = df["brightness"].values

# Sampling info
dt = t[1] - t[0]
fs = 1.0 / dt
N = len(brightness)

# Butterworth band-pass filter (40–180 bpm)
lowcut = low_bpm / 60.0
highcut = high_bpm / 60.0
nyq = 0.5 * fs
b, a = butter(
    N=4,
    Wn=[lowcut/nyq, highcut/nyq],
    btype="band"
)
filtered = filtfilt(b, a, brightness) #Filt filt filters forward and backward to reduce phase shift

# Compute FFT of filtered signal (0–3 Hz)
fft_vals = np.fft.fft(filtered)
freqs = np.fft.fftfreq(N, dt)
mask = (freqs >= 0) & (freqs <= 3)
freqs = freqs[mask]
fft_vals = fft_vals[mask]

# Find peak
peak_idx = np.argmax(np.abs(fft_vals))
peak_freq = freqs[peak_idx]
peak_amp = np.abs(fft_vals[peak_idx])
heart_rate_bpm = peak_freq * 60

# Plot time and frequency-domain
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Time domain
ax1.plot(t, brightness, label="Raw", alpha=0.5)
ax1.plot(t, filtered,  label="Filtered")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Brightness")
ax1.set_title("Time Domain: Raw vs. Filtered Signal")
ax1.legend()
ax1.grid(True)

# Frequency domain with peak line
ax2.plot(freqs, np.abs(fft_vals), linewidth=1)
ax2.axvline(peak_freq, color='red', linestyle='--',
            label=f'Peak: {peak_freq:.2f} Hz ({heart_rate_bpm:.0f} bpm)')
ax2.set_xlim(0, 3)
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Amplitude")
ax2.set_title("Frequency Domain: FFT of Filtered Signal (0–3 Hz)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

print(f"Estimated heart rate: {heart_rate_bpm:.1f} bpm")
