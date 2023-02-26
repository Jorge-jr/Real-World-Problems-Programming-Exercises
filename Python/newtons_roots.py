'''
Write a program that implements the Newton's method for finding roots of a given function. The Newton's method is a popular iterative method for finding the root of a function, and 
it can be used to solve a wide variety of mathematical problems.

Define a function f(x) that you want to find the root of. This function should take a single input parameter x and return a single output value.

Define another function f_derivative(x) that returns the derivative of f(x) with respect to x. You can either compute the derivative analytically or numerically using finite 
differences.

Define an initial guess x0 for the root of f(x).

Implement the Newton's method using the following formula: x1 = x0 - f(x0) / f_derivative(x0).

Repeat step 4 until the difference between x1 and x0 is smaller than a certain threshold value, such as 0.0001.

Print the final value of x1, which should be an approximation of the root of f(x).

Test your program with different functions and initial guesses to see how well it performs.

Bonus: Modify your program to handle cases where the Newton's method does not converge, for example when the derivative of f(x) becomes zero at some point or when the initial guess 
is too far from the actual root. Implement a maximum number of iterations and print an error message if the method does not converge within that number of iterations.
'''

def f_derivative(x):
    pass