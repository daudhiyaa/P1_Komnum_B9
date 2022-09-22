# numerical-computing
This lecture aims to study methods to find (approximate) roots of polynomials

### how to run
- clone the repo `git clone https://github.com/daudhiyaa/komnum.git`
- open the terminal, then run
- for .cpp file : `g++ fileName.cpp -o fileName` then write `./fileName`
- for .py file : `python3 fileName.py`

## 1. Bolzano Method
also called as the `Half Interval method`, the `Divide method`, the `Bisection method`, or the `Binary Cutting method`.

> The steps that must be carried out in the Bolzano method are:

1. Calculate the function on the same interval from `x` until the sign changes from `f(xn)` and `f(x(n+1))`. Or in other words: `f(xn) x f(x(n+1)) < 0`

2. The first estimate for the root of the equation can be obtained by: `xt = (xn + x(n+1)) / 2`

3. Perform an evaluation to determine in which interval the roots of the equation are:

    a. If `f(xn) * f(x(n+1)) < 0`

        then the root of the equation is in the first sub-interval, set x(n+1) = xt, and go to step 4

    b. If `f(xn) * f(x(n+1)) > 0`

        then the roots of the equation are in the second sub-interval, set xn = xt, and go to step 4

    c. If `f(xn) * f(x(n+1)) = 0`

        then the root of the equation is xt, and the calculation is complete

4. Return to step 2 to calculate the new approximate root value

5. If the value obtained in step 4 is in accordance with the specified constraints, then the process is complete, and `xt` is the root to be searched for.