# 71 to 7
# 70 to 12
# 71 to 22
# 72 to 27
# 71 to 31
# 72 to 37
# 73 to 42
# 71 to 47
# 72 to 52
# 71 to 57
# 67 to 60

####For RACHEL#####
import numpy as np

# List of (value, end_index) pairs
segments = [
    (71, 7),
    (70, 12),
    (71, 22),
    (72, 27),
    (71, 31),
    (72, 37),
    (73, 42),
    (71, 47),
    (72, 52),
    (71, 57),
    (67, 60)
]

vector = []

start = 0
for value, end in segments:
    vector.extend([value] * (end - start))
    start = end 

vector = np.array(vector)

print(vector)
print(vector.mean())



