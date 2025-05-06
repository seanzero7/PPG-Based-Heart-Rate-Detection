"""
    python RawSignal.py video.MOV --plot
"""

import cv2
import numpy as np
import pandas as pd
import argparse
from pathlib import Path
import matplotlib.pyplot as plt

# -------------------- CLI -------------------- #
parser = argparse.ArgumentParser()
parser.add_argument("video", type=str, help="Path to video file")
parser.add_argument("--plot", action="store_true", help="Show preview plot")
args = parser.parse_args()

# -------------------- Open video -------------------- #
cap = cv2.VideoCapture(args.video)
if not cap.isOpened():
    raise IOError(f"Could not open {args.video}")

fps = cap.get(cv2.CAP_PROP_FPS)
dt = 1.0 / fps                         # seconds per frame

timestamps = []
brightness = []

frame_idx = 0
while True:
    ok, frame = cap.read()
    if not ok:
        break

    # Extract green channel from entire frame
    green_channel = frame[:, :, 1]   # 1 == green channel
    mean_val = np.mean(green_channel)

    brightness.append(mean_val)
    timestamps.append(frame_idx * dt)
    frame_idx += 1

cap.release()

# -------------------- Save CSV -------------------- #
out_csv = Path(args.video).with_suffix(".csv")
pd.DataFrame({"t_sec": timestamps, "brightness": brightness}).to_csv(out_csv, index=False)
print(f"Saved {len(brightness)} samples → {out_csv}")

# -------------------- Optional quick-look plot -------------------- #
if args.plot:
    plt.figure(figsize=(10, 4))
    plt.plot(timestamps, brightness, linewidth=1)
    plt.xlabel("Time (s)")
    plt.ylabel("Mean green-channel value")
    plt.title("Raw brightness signal")
    plt.tight_layout()
    plt.show()
