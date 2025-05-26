#!/usr/bin/env python3
"""
Program: Lab #4 Integration and Testing
Lab Number: Lab #4
Version: 1.1
Developer: Сильченко Анна
Date: 2025-05-07

Purpose:
    This module provides a unified menu for testing various components of Lab #4 assignments.
    It imports and integrates functions from assignment1.py, assignment2.py, assignment3.py,
    assignment4.py, and assignment5.py, allowing the user to select which assignment demo to run.
    In particular, for Assignment 2 the text is read from a source file.
"""

import sys

def main_menu() -> int:
    """
    Display the main menu and return the user's choice.
    
    Returns:
        int: The user's menu choice.
    """
    print("\n--- Lab #4 Main Menu ---")
    print("1. Assignment 1: Student Records Serialization and Search")
    print("2. Assignment 2: Text Analysis and Processing from File")
    print("3. Assignment 3: Series Analysis and Plotting")
    print("4. Assignment 4: Geometric Figures and Visualization")
    print("5. Assignment 5: NumPy Array Operations and Statistics")
    print("6. Exit")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def run_assignment(choice: int):
    """
    Run the selected assignment based on the user's choice.
    
    Parameters:
        choice (int): The menu option selected by the user.
    """
    if choice == 1:
        import assignment1
        print("\nRunning Assignment 1:")
        # --- Begin Assignment 1 demo ---
        # Create sample students and initialize serializers.
        students = assignment1.create_sample_students()
        csv_serializer = assignment1.CSVStudentSerializer("students.csv")
        pickle_serializer = assignment1.PickleStudentSerializer("students.pkl")
        
        # Save student data to both CSV and Pickle files.
        csv_serializer.save(students)
        pickle_serializer.save(students)
        
        # Allow the user to choose which file to load data from.
        while True:
            source_choice = input("Select data source (enter 'csv' or 'pickle'): ").strip().lower()
            if source_choice in ['csv', 'pickle']:
                break
            else:
                print("Invalid input. Please enter 'csv' or 'pickle'.")
        
        if source_choice == 'csv':
            loaded_students = csv_serializer.load()
            print("\nStudents loaded from CSV:")
        else:
            loaded_students = pickle_serializer.load()
            print("\nStudents loaded from Pickle:")
            
        for stud in loaded_students:
            print(stud)
            
        # Perform search operations.
        street = input("\nEnter a street name to search: ")
        found_students = csv_serializer.search_by_street(street, loaded_students)
        print(f"Students living on {street}:")
        for stud in found_students:
            print(stud)
            
        try:
            house = int(input("Enter a house number to search: "))
            found_students = csv_serializer.search_by_house(house, loaded_students)
            print(f"Students living in house number {house}:")
            for stud in found_students:
                print(stud)
        except ValueError:
            print("Invalid house number.")
        # --- End Assignment 1 demo ---
        
    elif choice == 2:
        import assignment2
        print("\nRunning Assignment 2:")
        # Instead of manual text entry, prompt for a source file name.
        source_file = input("Enter the source text file name: ").strip()
        result_file = "text_analysis_report.txt"
        assignment2.analyze_text_file(source_file, result_file)
    
    elif choice == 3:
        import assignment3
        print("\nRunning Assignment 3:")
        # For Assignment 3, simply call the run_analysis() function.
        assignment3.run_analysis()
    
    elif choice == 4:
        import assignment4
        print("\nRunning Assignment 4:")
        # For Assignment 4, call the interactive function that handles input parameters,
        # drawing (with fill color) and annotating the figure with text from the keyboard.
        assignment4.run_assignment()
    
    elif choice == 5:
        import assignment5
        print("\nRunning Assignment 5:")
        assignment5.assignment5_demo()
    
    elif choice == 6:
        print("Exiting program.")
        sys.exit()

def main():
    """
    Main function for the integrated Lab #4 demo.
    """
    while True:
        choice = main_menu()
        run_assignment(choice)
        retry = input("\nDo you want to continue? (y/n): ").strip().lower()
        if retry not in ('y', 'yes', 'д', 'да'):
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
