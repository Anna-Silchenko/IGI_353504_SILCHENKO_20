"""
Lab Assignment: Python Lab 1 - Utility Functions
Version: 1.0
Developer: Anna Ivanova
Date: 2025-04-23

This module provides utility functions such as decorators and input validation helpers
to support the core functionalities.
"""

import time

def debug_decorator(func):
    """
    A decorator that prints debugging information about the function's execution.
    
    Parameters:
        func (callable): The function to be decorated.
        
    Returns:
        callable: The wrapped function that prints debug details when executed.
    """
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args} kwargs: {kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} completed in {end_time - start_time:.6f} seconds\n")
        return result
    return wrapper

def get_int_input(prompt: str) -> int:
    """
    Prompt the user for an integer input and validate the entry.
    
    Parameters:
        prompt (str): The message displayed to the user.
        
    Returns:
        int: The integer provided by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_float_input(prompt: str) -> float:
    """
    Prompt the user for a float input and validate the entry.
    
    Parameters:
        prompt (str): The message displayed to the user.
        
    Returns:
        float: The float number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid float number.")

def repeat_execution(prompt: str = "Do you want to repeat the operation? (y/n): ") -> bool:
    """
    Ask the user whether to repeat an operation without exiting the program.
    
    Parameters:
        prompt (str): The prompt message.
        
    Returns:
        bool: True if user chooses to repeat, False otherwise.
    """
    while True:
        ans = input(prompt).strip().lower()
        if ans in ('y', 'yes'):
            return True
        elif ans in ('n', 'no'):
            return False
        else:
            print("Invalid input. Please type 'y' or 'n'.")
