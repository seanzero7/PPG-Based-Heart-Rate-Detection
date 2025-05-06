# 53 to 16
# 54 to 21
# 57 to 26
# 60 to 36
# 56 to 41
# 57 to 46
# 58 to 51
# 57 to 60

import numpy as np
import matplotlib.pyplot as plt
# List of (value, end_index) pairs
segments = [
    (53, 16),
    (54, 21),
    (57, 25),
    (60, 36),
    (56, 41),
    (57, 46),
    (58, 51),
    (57, 60)
]

vector = []

start = 0
for value, end in segments:
    vector.extend([value] * (end - start))
    start = end 

vector = np.array(vector)

print(vector)
print(vector.mean())