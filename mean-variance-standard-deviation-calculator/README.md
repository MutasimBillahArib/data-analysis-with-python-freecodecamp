# 📊 Mean-Variance-Standard Deviation Calculator

This project contains a Python function that computes key statistical measures — mean, variance, standard deviation, max, min, and sum — for a 3×3 matrix derived from a list of 9 numbers.

## 🔍 About the Project

The function takes a list of exactly **nine numerical values**, reshapes it into a 3×3 NumPy array (matrix), and calculates the following statistics:
- Mean
- Variance
- Standard Deviation
- Maximum
- Minimum
- Sum

Each of these statistics is computed:
- Along the **columns** (axis 0),
- Along the **rows** (axis 1),
- Over the **entire matrix** (flattened).

The output is a dictionary containing lists of results for each of the above metrics.


## 🧮 Example Usage

```python
from mean_var_std_calculator import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)
```
**Expected Output:**

```
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[2.449..., 2.449..., 2.449...], [0.816..., 0.816..., 0.816...], 2.581...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## ⚠️ Input Validation

- The function raises a ValueError if the input list does not contain exactly 9 elements.


## 📚 Learning Outcome

This project demonstrates:

- Array manipulation using NumPy

- Axis-wise statistical calculations

- Clean, readable Python code with helper functions

- Input validation and error handling


## 👨‍💻 Author

**Mutasim Billah**  

🔗 [LinkedIn](https://www.linkedin.com/in/mmbillah804/)  
🔗 [GitHub](https://github.com/mmbillah804)

