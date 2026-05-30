import numpy as np

# ==========================================
# Python List Slicing (Creates a Copy)
# ==========================================

py_list = [1, 2, 3, 4, 5]

sub_list = py_list[1:4]

print("Original List:", py_list)
print("Sub List:", sub_list)

sub_list[0] = 200

print("\nAfter modifying sub_list:")
print("Sub List:", sub_list)
print("Original List:", py_list)

# ==========================================
# NumPy Slicing (Creates a View)
# ==========================================

numpy_array = np.array([1, 2, 3, 4, 5])

sub_array = numpy_array[1:4]

print("\nOriginal NumPy Array:", numpy_array)
print("Sub Array:", sub_array)

sub_array[0] = 200

print("\nAfter modifying sub_array:")
print("Sub Array:", sub_array)
print("Original Array:", numpy_array)

# ==========================================
# NumPy Copy
# ==========================================

numpy_array = np.array([1, 2, 3, 4, 5])

sub_array = numpy_array[1:4].copy()

sub_array[0] = 200

print("\nUsing .copy()")
print("Sub Array:", sub_array)
print("Original Array:", numpy_array)
