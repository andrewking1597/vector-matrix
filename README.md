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

# Simple Example
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

# Example with Fractions
Note: Floats are NOT supported at this time. Instead of using floats, enter non-integer values as fraction strings or Fraction objects
```python
from vectormatrixlib.matrix import *

# Using fraction strings
matrix1 = CoefficientMatrix([[2, 9, '7/10'], ['5/10', 1, 1]])
matrix1.rref()

# Using Fraction objects
matrix2 = CoefficientMatrix([[2, 9, Fraction(7,10)], [Fraction(5,10), 1, 1]])
matrix2.rref()

print('******* Matrix 1 *******')
matrix1.print_matrix()

print('******* Matrix 2 *******')
matrix2.print_matrix()
```

### Output
\*\*\*\*\*\*\* Matrix 1 \*\*\*\*\*\*\*

1        0        83/25

0        1        -33/50


\*\*\*\*\*\*\* Matrix 2 \*\*\*\*\*\*\*

1        0        83/25

0        1        -33/50

