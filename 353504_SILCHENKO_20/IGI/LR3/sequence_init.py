"""
Lab Assignment: Python Lab 1 - Sequence Initialization
Version: 1.0
Developer: Anna Ivanova
Date: 2025-04-23

This module provides functions for initializing a sequence. It includes two methods:
    - Using a generator to build a simple range based sequence.
    - Using user input to populate the sequence elements.
"""

def sequence_from_generator(size: int) -> list:
    """
    Generate a sequence of integers from 1 up to 'size' using a generator expression.
    
    Parameters:
        size (int): The number of elements in the sequence.
        
    Returns:
        list: A list containing integers from 1 to size.
    """
    return [i for i in range(1, size + 1)]

def sequence_from_input(size: int) -> list:
    """
    Create a sequence by prompting the user to input each element.
    
    Parameters:
        size (int): The number of elements in the sequence.
        
    Returns:
        list: A list of integers input by the user.
    """
    sequence = []
    print(f"Please enter {size} integer values:")
    for i in range(size):
        while True:
            try:
                value = int(input(f"Element {i+1}: "))
                sequence.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return sequence
