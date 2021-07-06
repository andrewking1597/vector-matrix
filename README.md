# vector-matrix
This package is a linear algebra tool for manipulating matrices.  However, in most cases you are better off using either [numpy.linalg](https://numpy.org/doc/stable/reference/routines.linalg.html) or [scipy.linalg](https://docs.scipy.org/doc/scipy/reference/linalg.html#module-scipy.linalg) -- both are much more robust than this project.

# Features
- Row-echelon and reduced row-echelon form of coefficient matrices
- Stores and displays values as fractions for maximum precision
- Prints matrices neatly, displayed with even rows and columns

# Installation
```
pip install vectormatrixlib==0.0.5
```

# Example
```python
from vectormatrixlib.matrix import *

my_matrix = CoefficientMatrix([[0, 5, 4, 3], [1, 6, 6, 4], [0, 0, 1, 2], [4, 0, 0, 0]])
my_matrix.rref()
my_matrix.print_matrix()
```
### Output
1    0    -1

0    1    2

0    0    0
