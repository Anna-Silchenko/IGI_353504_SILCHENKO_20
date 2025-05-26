#!/usr/bin/env python3
"""
Program: NumPy Array Operations and Statistics
Lab Number: Lab #4
Version: 1.0
Developer: Сильченко Анна
Date: 2025-05-07

Purpose:
    This module demonstrates the capabilities of the NumPy library when working with arrays,
    random number generation, and mathematical/statistical operations.
    It creates an integer matrix A[n, m] using random numbers, computes various statistics,
    sorts the elements of the last row in ascending order, and calculates the median of the last row
    both using the standard numpy function and by manual implementation.
"""

import numpy as np

def create_matrix(n: int, m: int) -> np.ndarray:
    """
    Create an integer matrix A of size n x m with random numbers.
    
    Parameters:
        n (int): Number of rows.
        m (int): Number of columns.
    
    Returns:
        np.ndarray: The created matrix.
    """
    # Generate random integers in the range 0 to 100.
    matrix = np.random.randint(0, 101, size=(n, m))
    return matrix

def compute_statistics(matrix: np.ndarray) -> dict:
    """
    Compute statistical measures on the entire matrix.
    
    Returns a dictionary containing:
        - mean: Mean value of matrix elements.
        - median: Median value of matrix elements.
        - variance: Variance of matrix elements.
        - std: Standard deviation of matrix elements.
        - corrcoef: Correlation coefficient matrix computed among rows (if applicable).
    
    Parameters:
        matrix (np.ndarray): The input matrix.
    
    Returns:
        dict: Dictionary with computed statistics.
    """
    stats = {}
    stats["mean"] = np.mean(matrix)
    stats["median"] = np.median(matrix)
    stats["variance"] = np.var(matrix)
    stats["std"] = np.std(matrix)
    # Compute correlation coefficient among rows if there are more than one row.
    if matrix.shape[0] > 1:
        stats["corrcoef"] = np.corrcoef(matrix)
    else:
        stats["corrcoef"] = None
    return stats

def sort_last_row(matrix: np.ndarray) -> np.ndarray:
    """
    Sort the elements of the last row of the matrix in ascending order.
    
    Parameters:
        matrix (np.ndarray): The input matrix.
    
    Returns:
        np.ndarray: Sorted last row.
    """
    last_row = matrix[-1, :]
    sorted_row = np.sort(last_row)
    return sorted_row

def manual_median(arr: np.ndarray) -> float:
    """
    Manually compute the median of a 1D numpy array.
    
    Parameters:
        arr (np.ndarray): 1D array of numbers.
    
    Returns:
        float: The median value computed manually.
    """
    a = np.sort(arr)
    n = len(a)
    if n % 2 == 1:
        return float(a[n // 2])
    else:
        return (float(a[n // 2 - 1]) + float(a[n // 2])) / 2

def display_matrix(matrix: np.ndarray):
    """
    Display the matrix.
    
    Parameters:
        matrix (np.ndarray): The matrix to display.
    """
    print("Matrix:")
    print(matrix)

def assignment5_demo():
    """
    Run the demonstration for NumPy array operations.
    
    This function prompts the user for matrix dimensions, creates a random matrix,
    computes statistics, sorts the last row, and computes the median of the last row
    using both numpy and a manual calculation.
    """
    while True:
        try:
            n = int(input("Enter the number of rows for the matrix: "))
            m = int(input("Enter the number of columns for the matrix: "))
            if n <= 0 or m <= 0:
                print("Both dimensions must be positive integers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter valid integer numbers.")

    matrix = create_matrix(n, m)
    display_matrix(matrix)

    stats = compute_statistics(matrix)
    print("\nStatistical Measures for the entire matrix:")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Median: {stats['median']:.2f}")
    print(f"Variance: {stats['variance']:.2f}")
    print(f"Standard Deviation: {stats['std']:.2f}")
    if stats["corrcoef"] is not None:
        print("Correlation Coefficient Matrix among rows:")
        print(stats["corrcoef"])

    sorted_last_row = sort_last_row(matrix)
    print("\nSorted last row of the matrix:")
    print(sorted_last_row)

    # Calculate median of the last row using np.median and manual calculation.
    np_median = np.median(matrix[-1, :])
    manual_med = manual_median(matrix[-1, :])
    print(f"\nMedian of the last row (using np.median): {np_median:.2f}")
    print(f"Median of the last row (manual calculation): {manual_med:.2f}")

if __name__ == "__main__":
    assignment5_demo()
