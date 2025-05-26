#!/usr/bin/env python3
"""
Program: Student Records Serialization and Search
Lab Number: Lab #4
Version: 1.0
Developer: Сильченко Анна
Date: 2025-05-07

Purpose:
    This module manages student records using file serialization.
    It provides functionalities to store student records in CSV and Pickle formats,
    and to perform searches and sorting of records based on street and house number.
"""

import csv
import pickle
import os

class Student:
    """
    A class representing a student record.
    
    Attributes:
        surname (str): Student's surname.
        street (str): Student's street.
        house (int): House number.
        apartment (int): Apartment number.
    """
    
    # Static attribute: count of student instances
    total_students = 0

    def __init__(self, surname: str, street: str, house: int, apartment: int):
        self.surname = surname
        self.street = street
        self.house = house
        self.apartment = apartment
        Student.total_students += 1

    def __str__(self):
        return f"{self.surname}, {self.street}, House {self.house}, Apt {self.apartment}"

    def __repr__(self):
        return f"Student({self.surname}, {self.street}, {self.house}, {self.apartment})"

    def __lt__(self, other):
        """Implement less-than operator for sorting by surname."""
        return self.surname < other.surname

class StudentSerializer:
    """
    Base class for student record serialization.
    """

    def __init__(self, filename: str):
        self.filename = filename

    def save(self, students: list):
        """
        Save student records.
        Should be implemented in the derived classes.
        """
        raise NotImplementedError

    def load(self) -> list:
        """
        Load student records.
        Should be implemented in the derived classes.
        """
        raise NotImplementedError

    def search_by_street(self, street: str, students: list) -> list:
        """
        Return list of students living on the given street.
        """
        return [s for s in students if s.street.lower() == street.lower()]

    def search_by_house(self, house: int, students: list) -> list:
        """
        Return list of students living in the given house number.
        """
        return [s for s in students if s.house == house]

class CSVStudentSerializer(StudentSerializer):
    """
    CSV serializer for student records.
    """
    def save(self, students: list):
        with open(self.filename, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["surname", "street", "house", "apartment"])
            for student in students:
                writer.writerow([student.surname, student.street, student.house, student.apartment])

    def load(self) -> list:
        students = []
        if not os.path.exists(self.filename):
            return students
        with open(self.filename, "r", newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    student = Student(row["surname"], row["street"], int(row["house"]), int(row["apartment"]))
                    students.append(student)
                except (ValueError, KeyError) as e:
                    print("Error reading row:", row, ":", e)
        return students

class PickleStudentSerializer(StudentSerializer):
    """
    Pickle serializer for student records.
    """
    def save(self, students: list):
        with open(self.filename, "wb") as pfile:
            pickle.dump(students, pfile)

    def load(self) -> list:
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "rb") as pfile:
            students = pickle.load(pfile)
        return students

def create_sample_students() -> list:
    """
    Create a sample list of Student objects.
    """
    return [
        Student("Ivanov", "Lenina", 10, 101),
        Student("Petrov", "Kirova", 15, 202),
        Student("Sidorov", "Lenina", 10, 102),
        Student("Smirnov", "Pushkina", 7, 303),
        Student("Silchenko", "Alferova", 10, 31),
        Student("Dzichkovskaya", "Alferova", 10, 293)
    ]
