# numerical-computing
### how to run
- clone the repo 
```
git clone https://github.com/daudhiyaa/komnum.git
```
- open the terminal, then run
- for .cpp file : `g++ fileName.cpp -o fileName` then write `./fileName`
- for .py file : `python3 fileName.py`

## Methods to find (approximate) roots of polynomials
### 1. Bolzano Method
also called as:

- the `Half Interval method`
- the `Divide method`
- the `Bisection method`
- or the `Binary Cutting method`.

> The steps that must be carried out in the Bolzano method are:

1. Calculate the function on the same interval from `x` until the sign changes from `f(x1)` and `f(x2)`. Or in other words: `f(x1) * f(x2) < 0`

2. The first estimate for the root of the equation can be obtained by: `x3 = (x1 + x2) / 2`

3. Perform an evaluation to determine in which interval the roots of the equation are:

    * If `f(x1) * f(x3) < 0`
    
        then the root of the equation is in the first sub-interval, set x1 = x3, and go to step 4

    * If `f(x2) * f(x3) < 0`

        then the roots of the equation are in the second sub-interval, set x2 = x3, and go to step 4

    * If `f(xn) = 0`

        then the root of the equation is `xn`, and the calculation is complete

4. Return to step 2 to calculate the new approximate root value

5. If no constraint is specified, and the value obtained in step 4 is close with 0, then search the `min(abs(f(xn)))` and the process is complete, and `xn` is the root to be searched for.

6. If the value obtained in step 4 is in accordance with the specified constraints, then the process is complete, and `x3` is the root to be searched for.