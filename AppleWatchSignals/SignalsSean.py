# 64 to 8
# 66 to 14
# 65 to 19
# 63 to 24
# 62 to 34
# 60 to 53
# 62 to 60


import numpy as np

# List of (value, end_index) pairs
segments = [
    (64, 8),
    (66, 14),
    (65, 19),
    (63, 24),
    (62, 34),
    (60, 53),
    (62, 60),
]


vector = []

start = 0
for value, end in segments:
    vector.extend([value] * (end - start))
    start = end 

vector = np.array(vector)

print(vector)
print(vector.mean())