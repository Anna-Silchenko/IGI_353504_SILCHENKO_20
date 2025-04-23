"""
Lab Assignment: Standard data types, collections, functions, modules.
Version: 2.0
Developer: Silchenko Anna Andreevna
Date: 2025-04-10

This main module integrates functionalities for several tasks:
    1. Calculate series expansion for 1/(1-x)
    2. Sum of a sequence of numbers with two initialization methods:
         a) Manual input (cycle ends when a negative number is entered)
         b) Generator (a sequence of integers from 1 to N is created)
    3. Count characters in the range 'f' to 'y' in the input text
    4. Analyze a given text:
         a) Count words enclosed in quotes.
         b) Determine letter frequency (case-insensitive).
         c) Output comma-separated phrases in alphabetical order.
    5. Process a list of floats:
         - Find the element with maximum absolute value.
         - Calculate the sum of elements between the first and second negative elements.
    6. Exit
"""

from business_functions import calculate_series, print_series_table
from sequence_init import sequence_from_generator 
from utils import get_int_input, get_float_input, repeat_execution


def sum_sequence_manual() -> int:
    """
    Reads integers from user input and returns their sum.
    The input loop terminates when a negative number is entered
    (the negative number is not included in the sum).
    """
    total = 0
    while True:
        try:
            num = int(input("Enter an integer (negative to stop): "))
        except ValueError:
            print("Invalid input, please enter an integer.")
            continue
        if num < 0:
            break
        total += num
    return total


def sum_sequence_combined():
    """
    Offers a choice between two initialization methods for a sequence of numbers:
      1. Manual input: a cycle receiving integers until a negative number is entered.
      2. Generator: the sequence is automatically generated (integers from 1 to N, where N is provided by the user).
    The sum of elements is then computed and displayed.
    """
    print("\nChoose the initialization method for the sequence:")
    print("1. Manual input (enter integers; negative number stops the input)")
    print("2. Generator (sequence of integers from 1 to N)")
    method = get_int_input("Enter your choice (1 or 2): ")
    
    if method == 1:
        s = sum_sequence_manual()
        print("The sum of the entered sequence is:", s)
    elif method == 2:
        size = get_int_input("Enter the size of the sequence: ")
        seq = sequence_from_generator(size)
        s = sum(seq)
        print("Sequence generated using generator:", seq)
        print("The sum of the generated sequence is:", s)
    else:
        print("Invalid choice. Returning to the main menu.")


def count_chars_in_range():
    """
    Reads a line of text from the user and counts the characters that lie in the range from 'f' to 'y' (inclusive).
    The search is case-insensitive.
    """
    text = input("Enter a text: ")
    count = 0
    for ch in text.lower():
        if 'f' <= ch <= 'y':
            count += 1
    print(f"Number of characters in the range 'f' to 'y': {count}")


def count_quoted_words(text: str) -> int:
    """
    Counts the number of words in the text that are enclosed in quotation marks.
    Both standard double quotes (") and guillemets (« ») are considered.
    
    Parameters:
        text (str): The input text.
    
    Returns:
        int: The number of words enclosed in quotes.
    """
    count = 0
    words = text.split()
    for word in words:
        word_stripped = word.strip(' ,.!?;:')
        if (word_stripped.startswith('"') and word_stripped.endswith('"')) or \
           (word_stripped.startswith('«') and word_stripped.endswith('»')):
            count += 1
    return count


def letter_frequency(text: str) -> dict:
    """
    Calculates the frequency of each letter in the text (ignoring case).
    
    Parameters:
        text (str): The input text.
    
    Returns:
        dict: A dictionary mapping letters to their frequencies.
    """
    freq = {}
    for ch in text.lower():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def sorted_comma_phrases(text: str) -> list:
    """
    Splits the text by commas, trims whitespace, and returns the resulting phrases 
    sorted in alphabetical order (case-insensitive).
    
    Parameters:
        text (str): The input text.
    
    Returns:
        list: An alphabetically sorted list of phrases.
    """
    phrases = [phrase.strip() for phrase in text.split(',') if phrase.strip()]
    return sorted(phrases, key=lambda s: s.lower())


def analyze_given_string():
    """
    Analyzes a predefined text string by:
        a) Counting the number of words enclosed in quotes.
        b) Determining the frequency of each letter (case-insensitive).
        c) Outputting, in alphabetical order, all comma-separated phrases.
    The predefined text is hard-coded in the function.
    """
    text = ("So she was considering in her own mind, as well as she could, for the hot day made her feel "
            "very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of "
            "getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")
    
    print("\nAnalyzing the predefined text:")
    print(text)
    
    # (a) Count words enclosed in quotes.
    quoted_count = count_quoted_words(text)
    print("\nSubtask (a): Number of words enclosed in quotes:", quoted_count)
    
    # (b) Letter frequency.
    freq = letter_frequency(text)
    print("\nSubtask (b): Letter frequency:")
    for letter in sorted(freq.keys()):
        print(f"{letter}: {freq[letter]}")
    
    # (c) Comma-separated phrases in alphabetical order.
    phrases = sorted_comma_phrases(text)
    print("\nSubtask (c): Comma-separated phrases in alphabetical order:")
    for phrase in phrases:
        print(phrase)


def input_float_list() -> list:
    """
    Prompts the user to input a list of floating-point numbers with validation.
    
    Returns:
        list: The list of floats entered by the user.
    """
    size = get_int_input("Enter the number of elements in the float list: ")
    float_list = []
    for i in range(size):
        value = get_float_input(f"Enter element {i + 1}: ")
        float_list.append(value)
    return float_list


def process_float_list():
    """
    Processes a list of floating-point numbers by:
      1. Displaying the entered list.
      2. Finding the element with maximum absolute value.
      3. Calculating the sum of elements between the first and second negative numbers.
         (If there are fewer than two negatives, the sum is not computed.)
    """
    float_list = input_float_list()
    print("\nFloat list:", float_list)
    
    if not float_list:
        print("The list is empty.")
        return
    
    # 1. Maximum by absolute value.
    max_abs_element = max(float_list, key=abs)
    print("Max absolute element in the list:", max_abs_element)
    
    # 2. Sum of elements between the first and second negative numbers.
    neg_indices = [i for i, num in enumerate(float_list) if num < 0]
    if len(neg_indices) < 2:
        print("There are less than two negative elements; cannot compute sum between negatives.")
    else:
        first_neg = neg_indices[0]
        second_neg = neg_indices[1]
        if second_neg - first_neg <= 1:
            sum_between = 0
        else:
            sum_between = sum(float_list[first_neg + 1:second_neg])
        print("Sum of elements between the first and second negative elements:", sum_between)


def menu():
    """
    Displays the main menu and handles the selection of tasks to execute.
    """
    while True:
        print("\n--- Comprehensive Python Lab Menu ---")
        print("1. Calculate series expansion for 1/(1-x)")
        print("2. Sum of a sequence of numbers (choose initialization method)")
        print("3. Count characters in the range 'f' to 'y' in input text")
        print("4. Analyze a given text (quotes, letter frequency, comma-separated phrases)")
        print("5. Process float list (max absolute element and sum between negatives)")
        print("6. Exit")
        
        choice = get_int_input("Enter your choice (1-6): ")
        
        if choice == 1:
            try:
                x = get_float_input("Enter the value of x (|x| < 1): ")
                if abs(x) >= 1:
                    print("Error: x must be less than 1 in absolute value for series convergence.")
                    continue
                eps = get_float_input("Enter the desired accuracy (eps): ")
                result = calculate_series(x, eps)
                print_series_table(result)
            except Exception as e:
                print("An error occurred:", e)
        elif choice == 2:
            sum_sequence_combined()
        elif choice == 3:
            count_chars_in_range()
        elif choice == 4:
            analyze_given_string()
        elif choice == 5:
            process_float_list()
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option between 1 and 6.")
        
        if not repeat_execution():
            print("Exiting the program. Goodbye!")
            break


if __name__ == "__main__":
    menu()
