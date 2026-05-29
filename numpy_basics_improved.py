# =============================================================
# NumPy Fundamentals — Portfolio Notebook
# Author: anujakharat7
# Date: May 2026
# Topics: Array creation, speed/memory comparison, built-in
#         functions, array properties
# =============================================================

# ── Cell 1: Imports ──────────────────────────────────────────
import numpy as np
import time
import sys


# ── Cell 2 (Markdown) ────────────────────────────────────────
# ## Why NumPy?
# NumPy arrays are stored in contiguous memory blocks and use
# fixed data types, making them significantly faster and more
# memory-efficient than Python lists for numerical operations.


# ── Cell 3: Speed Comparison — Python List vs NumPy Array ────
SIZE = 1_000_000

# Python list
start = time.perf_counter()
py_list = [1, 2, 3, 4]
sq_list = [i ** 2 for i in range(SIZE)]
end = time.perf_counter()
print(f"Python list  time = {end - start:.6f} seconds")

# NumPy array
start = time.perf_counter()
np_array = np.arange(SIZE)
sq_array = np_array ** 2
end = time.perf_counter()
print(f"NumPy array  time = {end - start:.6f} seconds")
# Result: NumPy is typically 10–100x faster due to vectorization


# ── Cell 4 (Markdown) ────────────────────────────────────────
# ## Memory Comparison
# Python lists store pointers to objects; each element has
# overhead. NumPy arrays store raw numeric bytes — much leaner.


# ── Cell 5: Memory Comparison ────────────────────────────────
sample_list = list(range(1000))
sample_array = np.arange(1000)

list_memory = sys.getsizeof(sample_list[0]) * len(sample_list)
array_memory = sample_array.nbytes

print(f"Python list  size = {list_memory} bytes")
print(f"NumPy array  size = {array_memory} bytes")
print(f"NumPy is ~{list_memory // array_memory}x more memory-efficient")


# ── Cell 6 (Markdown) ────────────────────────────────────────
# ## Creating Arrays
# NumPy supports multiple dtypes. Mixing types causes upcasting:
# all elements are converted to the most general type.


# ── Cell 7: Array Creation & dtype ───────────────────────────
# Integer array
arr_int = np.array([1, 2, 3, 4])
print("Integer array:", arr_int, "| dtype:", arr_int.dtype)

# Mixed types → upcasting to Unicode string
arr_mixed = np.array([1, 3, 5, "abc"])
print("Mixed array: ", arr_mixed, "| dtype:", arr_mixed.dtype)
# Note: NumPy upcasts to <U21 (Unicode string) to fit all elements


# ── Cell 8: 2D Array ─────────────────────────────────────────
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("2D Array:\n", arr_2d)
print("Shape:", arr_2d.shape)   # (rows, columns)


# ── Cell 9 (Markdown) ────────────────────────────────────────
# ## Built-in Array Creation Functions
# NumPy provides fast initializers — useful in ML for weight
# initialization and creating placeholder tensors.


# ── Cell 10: zeros, ones, full ───────────────────────────────
zeros = np.zeros((2, 3), dtype="int64")
ones  = np.ones((4, 4),  dtype="float")
full  = np.full((3, 4), fill_value=7)

print("zeros:\n", zeros, "\nshape:", zeros.shape)
print("\nones:\n",  ones,  "\nshape:", ones.shape)
print("\nfull:\n",  full,  "\nshape:", full.shape)


# ── Cell 11: Identity Matrix (np.eye) ────────────────────────
# The identity matrix is used in linear algebra (ML weight init,
# matrix inversion checks, etc.)
identity = np.eye(5)
print("Identity matrix (5x5):\n", identity)
print("Shape:", identity.shape)


# ── Cell 12: np.arange vs np.linspace ────────────────────────
# arange  → fixed step size (like Python range)
# linspace → fixed number of evenly-spaced points

arange_arr  = np.arange(0, 11, 2)
linspace_arr = np.linspace(0, 100, 4)

print("arange (0 to 10, step 2):", arange_arr)
print("linspace (0 to 100, 4 points):", linspace_arr)
# Key difference: linspace guarantees the end value is included


# ── Cell 13 (Markdown) ───────────────────────────────────────
# ## Array Properties
# Understanding shape, size, ndim, and dtype is essential for
# debugging data pipelines and model input shapes.


# ── Cell 14: Array Properties ────────────────────────────────
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Array:\n", arr)
print("shape :", arr.shape)   # (rows, cols)
print("size  :", arr.size)    # total elements
print("ndim  :", arr.ndim)    # number of dimensions
print("dtype :", arr.dtype)   # data type


# ── Cell 15 (Markdown) ───────────────────────────────────────
# ## Summary
# | Feature        | Python List | NumPy Array |
# |----------------|-------------|-------------|
# | Speed          | Slow        | Fast        |
# | Memory         | High        | Low         |
# | Element types  | Mixed       | Homogeneous |
# | Math ops       | Manual loop | Vectorized  |
#
# NumPy is the foundation of pandas, scikit-learn, TensorFlow,
# and PyTorch — mastering it is essential for any AI/ML role.
