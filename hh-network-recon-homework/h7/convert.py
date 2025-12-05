import numpy as np

# Input URH file (.complex16s)
data = np.fromfile("input.complex16s", dtype=np.int16)


iq = data.astype(np.float32) / 256.0  
iq8 = iq.astype(np.int8)

# Save rtl_433 compatible file
iq8.tofile("output.cs8")

print("Conversion complete → output.cs8")