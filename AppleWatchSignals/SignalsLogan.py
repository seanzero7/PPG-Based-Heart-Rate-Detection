# 66 to 8
# 64 to 24
# 67 to 34
# 66 to 39
# 71 to 44
# 72 to 49
# 70 to 59
# 71 to 60

import numpy as np

# List of (value, end_index) pairs
segments = [
    (68, 9),
    (69, 14),
    (67, 20),
    (64, 24),
    (63, 29),
    (62, 34),
    (63, 45),
    (62, 50),
    (61, 55),
    (62, 60)
]
vector = []

start = 0
for value, end in segments:
    vector.extend([value] * (end - start))
    start = end

vector = np.array(vector)
print(vector)
print(vector.mean())