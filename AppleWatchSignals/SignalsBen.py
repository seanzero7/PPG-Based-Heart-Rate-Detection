# 91 to 8
# 90 to 13
# 88 to 19
# 87 to 29
# 86 to 34
# 92 to 44
# 89 to 49
# 91 to 60

import numpy as np

# List of (value, end_index) pairs
segments = [
    (91, 8),
    (90, 13),
    (88, 19),
    (87, 29),
    (86, 34),
    (92, 44),
    (89, 49),
    (91, 60),
]


vector = []


start = 0
for value, end in segments:
    vector.extend([value] * (end - start))
    start = end 

vector = np.array(vector)

print(vector)
print(vector.mean())