import math
from utils import debug_decorator

@debug_decorator
def calculate_series(x: float, eps: float) -> tuple:
    """
    Calculate the series expansion of the function f(x) = 1/(1-x)
    using the power series: f(x) = 1 + x + x^2 + ... for |x| < 1,
    up to a maximum of 500 iterations.

    The function accumulates terms until the absolute error between the
    computed series sum and the exact value (using math) is less than eps.

    Parameters:
        x (float): The input value, must satisfy |x| < 1.
        eps (float): The desired accuracy (error threshold).

    Returns:
        tuple: A tuple containing:
            - x (float): The input value.
            - n (int): The number of terms summed.
            - series_sum (float): The computed sum from the series.
            - exact_value (float): The exact function value computed as 1/(1-x).
            - eps (float): The used accuracy threshold.

    Raises:
        ValueError: If |x| >= 1 (series does not converge).
    """
    if abs(x) >= 1:
        raise ValueError("x must be less than 1 in absolute value for series convergence.")

    series_sum = 0.0
    n = 0
    error = math.inf
    exact_value = 1 / (1 - x)

    while error > eps and n < 500:
        term = x ** n
        series_sum += term
        error = abs(exact_value - series_sum)
        n += 1

    return (x, n, series_sum, exact_value, eps)

def print_series_table(result: tuple):
    """
    Print the result of the series calculation in a formatted table.
    
    The table has the columns:
        x, n, F(x) (series value), Math F(x) (exact value) and eps.
    
    Parameters:
        result (tuple): A tuple containing (x, n, series_sum, exact_value, eps).
    """
    x, n, series_sum, exact_value, eps = result
    header = f"{'x':>10} | {'n':>5} | {'F(x)':>15} | {'Math F(x)':>15} | {'eps':>10}"
    separator = "-" * len(header)
    row = f"{x:10.4f} | {n:5d} | {series_sum:15.8f} | {exact_value:15.8f} | {eps:10.8f}"
    
    print(separator)
    print(header)
    print(separator)
    print(row)
    print(separator)
