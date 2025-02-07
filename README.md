# Infinite Recursion Bug in Python Factorial Function

This repository demonstrates a common error in recursive functions:  infinite recursion. The `bug.py` file contains a factorial function that works correctly for non-negative inputs but throws a `RecursionError` when given a negative number.  The solution (`bugSolution.py`) adds a check to prevent this error.

This example highlights the importance of defining a complete base case in recursive functions to avoid stack overflow issues.