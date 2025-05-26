#!/usr/bin/env python3
"""
Program: Series Expansion and Analysis with Precision
Lab Number: Lab #4, Task 3 (Revised)
Version: 1.1
Developer: Silchenko Anna
Date: 2025-05-07

Purpose:
    Computes the function f(x)=1/(1-x) using its power series expansion.
    The summation stops when the absolute difference between the computed series value
    and the exact value becomes less than the specified precision (eps) or when
    the number of terms reaches 500.
    
    The program outputs a table (with one row) showing:
      x | n | F(x) (Series) | Math F(x) | eps
      
    It then calculates additional statistical parameters for the single computed value.
    
    Finally, it uses matplotlib to plot two continuous graphs on the same axes:
      - The exact function f(x)=1/(1-x) calculated using math.
      - The series approximation function defined as Sₙ(x)=∑₍ᵢ₌₀₎⁽ⁿ⁻¹⁾ xⁱ, where n is the number of terms determined
        for the input x.
        
    This graph is drawn over an interval (e.g. from -0.9 to 0.9), includes axes labels, legend, grid, annotations,
    and is saved to a file.
"""

import math
import statistics
import matplotlib.pyplot as plt
import numpy as np

class SeriesAnalyzer:
    def __init__(self, result):
        """
        Initialize with a dictionary containing:
          - 'x': input value (|x| < 1)
          - 'n': number of terms used in the series
          - 'F_series': series expansion value for the given x
          - 'F_math': exact function value computed as 1/(1-x)
          - 'eps': desired precision
        """
        self.result = result

    def compute_statistics(self):
        """
        Since only one computed value is available, statistics are trivial.
        Returns a dictionary containing:
            'mean', 'median', 'mode', 'variance', 'stdev'
        For a single number, they all equal that number (or 0 for variance and stdev).
        """
        value = self.result['F_series']
        stats = {
            'mean': value,
            'median': value,
            'mode': value,
            'variance': 0.0,
            'stdev': 0.0
        }
        return stats

    def plot_results(self, n_terms, save_filename="series_plot.png"):
        """
        Plot the exact function and the series approximation (with fixed n_terms) over an interval.
        
        The series approximation function is defined as:
            Sₙ(x) = sum_{i=0}^{n_terms-1} x^i
        which is used to approximate f(x)=1/(1-x) for arbitrary x.
        
        A continuous curve for f(x) is plotted using math,
        and the series approximation is plotted using the computed number of terms.
        
        Parameters:
            n_terms (int): Number of terms to use in the series approximation function.
            save_filename (str): Filename for saving the resulting plot.
        """
        # Define a plotting interval where |x| < 1. Here we take from -0.9 to 0.9.
        x_values = np.linspace(-0.9, 0.9, 300)
        y_exact = [1 / (1 - t) for t in x_values]
        # Define the series approximation with fixed n_terms:
        def series_approx(t):
            s = sum([t ** i for i in range(n_terms)])
            return s
        y_series = [series_approx(t) for t in x_values]
        
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_exact, 'r-', label="Exact Calculation (math)")
        plt.plot(x_values, y_series, 'b--', label=f"Series Approximation (n={n_terms})")
        plt.xlabel("x")
        plt.ylabel("F(x)")
        plt.title("Exact Function vs Series Approximation for f(x)=1/(1-x)")
        plt.legend()
        plt.grid(True)
        # Optionally annotate a few sample points:
        for t in np.linspace(-0.8, 0.8, 5):
            plt.annotate(f"{series_approx(t):.2f}", (t, series_approx(t)), textcoords="offset points", xytext=(0, 8), ha="center")
        plt.savefig(save_filename)
        plt.show()

def compute_series_with_precision(x, eps, max_iter=500):
    """
    Compute the power series expansion for f(x)=1/(1-x) with a given accuracy (eps).
    The summation stops when |F_series - F_exact| < eps or when the number of terms reaches max_iter.
    
    Parameters:
        x (float): Input value (|x| < 1).
        eps (float): Desired precision.
        max_iter (int): Maximum number of terms (default is 500).
    
    Returns:
        tuple: (F_series, n) where F_series is the computed series value and n is the number of terms used.
    """
    F_exact = 1 / (1 - x)
    series_sum = 1.0  # First term (x^0 = 1)
    term = 1.0
    n = 1
    for i in range(1, max_iter):
        term *= x
        series_sum += term
        n += 1
        if abs(series_sum - F_exact) < eps:
            break
    return series_sum, n

def run_analysis():
    """
    Main function that:
      1. Reads a single value of x (|x| < 1) and the desired precision (eps).
      2. Computes f(x) using the power series expansion (with precision control) and using math.
      3. Outputs a table showing: x, n, F(x) (Series), Math F(x), eps.
      4. Computes and prints basic statistical parameters (for the one computed value).
      5. Plots two continuous graphs over an interval:
           - The exact function f(x)=1/(1-x) (using math)
           - The series approximation function Sₙ(x)=∑₍ᵢ₌₀₎^(n-1) xⁱ (using the computed n)
         The graph is saved to a file.
    """
    # Input a single x and eps
    while True:
        try:
            x = float(input("Enter a value for x (|x| < 1): "))
            if abs(x) >= 1:
                print("x must satisfy |x| < 1. Try again.")
                continue
            eps = float(input(f"Enter desired precision (eps) for x = {x}: "))
            if eps <= 0:
                print("eps must be positive. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
    # Compute series value and number of terms
    F_series, n_terms = compute_series_with_precision(x, eps)
    F_math = 1 / (1 - x)
    
    # Print a results table (only one row)
    print("\n|     x     |    n    |   F(x) (Series)   |   Math F(x)   |   eps   |")
    print("|-----------|---------|-------------------|---------------|---------|")
    print(f"| {x:^9.5f} | {n_terms:^7d} | {F_series:^17.6f} | {F_math:^13.6f} | {eps:^7.5f} |")
    
    # Create a result dictionary for statistics and further plotting.
    result = {
        'x': x,
        'n': n_terms,
        'F_series': F_series,
        'F_math': F_math,
        'eps': eps
    }
    
    analyzer = SeriesAnalyzer(result)
    stats = analyzer.compute_statistics()
    print("\nStatistical parameters for the computed series value:")
    print("Mean:", stats['mean'])
    print("Median:", stats['median'])
    print("Mode:", stats['mode'])
    print("Variance:", stats['variance'])
    print("Standard Deviation:", stats['stdev'])
    
    # Plot the functions over an interval using computed n_terms
    analyzer.plot_results(n_terms)

if __name__ == "__main__":
    run_analysis()
