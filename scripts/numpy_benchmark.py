import numpy as np
import time

size = 2000

A = np.random.rand(size, size)
B = np.random.rand(size, size)

start = time.perf_counter()

C = A @ B

end = time.perf_counter()

print("Matrix size:", size, "x", size)
print("Runtime:", end - start, "seconds")