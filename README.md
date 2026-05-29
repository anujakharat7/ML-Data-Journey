# ML-Data-Journey
Hands-on notebooks covering NumPy, Pandas, Matplotlib, and Machine Learning basics. Topics include array operations, data cleaning, visualization, and ML algorithms. Python | Jupyter | scikit-learn.
# 01 — NumPy Fundamentals

**Date:** May 2026  
**Topics:** Array creation, dtype, speed & memory comparison, built-in functions, array properties

---

## What This Covers

| Concept | Description |
|---|---|
| Speed comparison | Python list vs NumPy array using `time.perf_counter()` |
| Memory comparison | `sys.getsizeof` vs `.nbytes` |
| Array creation | `np.array`, `np.zeros`, `np.ones`, `np.full`, `np.eye` |
| Range functions | `np.arange` vs `np.linspace` — key differences |
| Array properties | `.shape`, `.size`, `.ndim`, `.dtype` |
| dtype & upcasting | What happens when you mix types in an array |

---

## Key Insight

NumPy arrays are stored in **contiguous memory** with **fixed dtypes**, making them:
- ~10–100× faster than Python lists for numerical operations
- ~8× more memory-efficient per element

This is why NumPy is the foundation of pandas, scikit-learn, TensorFlow, and PyTorch.

---

## How to Run

```bash
jupyter notebook numpy_basics.ipynb
```

Or open directly in JupyterLab.

---


