#!/usr/bin/env python3
"""
Program: Geometric Figures and Visualization
Lab Number: Lab #4
Version: 1.1
Developer: Сильченко Анна
Date: 2025-05-07

Purpose:
    This module defines base and derived classes for geometric figures.
    It includes an abstract base class for geometric figures, a color class,
    and derived classes such as Rectangle along with functions to draw both a rectangle
    and a parallelogram.
    
    In addition to the basic requirements, the drawing functions have been updated 
    to annotate the figure with a text provided by the user.
"""

import math
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class GeometricFigure(ABC):
    """
    Abstract base class for geometric figures.
    """
    @abstractmethod
    def area(self) -> float:
        """
        Compute and return the area of the figure.
        """
        pass

class FigureColor:
    """
    Class to store and manage the color of a geometric figure.
    
    Utilizes a property for color access and validation.
    """
    def __init__(self, color: str):
        self._color = color

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new_color: str):
        self._color = new_color

class Rectangle(GeometricFigure):
    """
    Rectangle class inherits from GeometricFigure.
    
    Attributes:
        width (float): Width of the rectangle.
        height (float): Height of the rectangle.
        color_obj (FigureColor): An object storing the rectangle's color.
    """
    # Class variable: name of the figure.
    name = "Rectangle"
    
    def __init__(self, width: float, height: float, color: str):
        self.width = width
        self.height = height
        self.color_obj = FigureColor(color)

    def area(self) -> float:
        """
        Compute the area of the rectangle.
        
        Returns:
            float: Computed area.
        """
        return self.width * self.height

    def __str__(self):
        return "Rectangle(width={0}, height={1}, color={2}, area={3:.2f})".format(
            self.width, self.height, self.color_obj.color, self.area()
        )

    @classmethod
    def figure_name(cls):
        """
        Return the name of the figure.
        
        Returns:
            str: Figure name.
        """
        return cls.name

def draw_rectangle(rect: Rectangle, annotation: str = "", save_filename: str = "rectangle.png"):
    """
    Draw the rectangle using matplotlib, fill it with its color, annotate it with the provided text,
    and save the image.
    
    Parameters:
        rect (Rectangle): The rectangle object to draw.
        annotation (str): Text to annotate on the figure.
        save_filename (str): Filename for saving the image.
    """
    fig, ax = plt.subplots()
    patch = patches.Rectangle((0, 0), rect.width, rect.height, edgecolor='black', facecolor=rect.color_obj.color)
    ax.add_patch(patch)
    
    # Set limits with some margins.
    ax.set_xlim(-1, rect.width + 1)
    ax.set_ylim(-1, rect.height + 1)
    ax.set_aspect('equal')
    
    plt.title(str(rect))
    
    # If annotation text is provided, show it at the center of the rectangle.
    if annotation:
        mid_x = rect.width / 2
        mid_y = rect.height / 2
        plt.text(mid_x, mid_y, annotation, fontsize=12, color='black',
                 ha="center", va="center", bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))
    
    plt.savefig(save_filename)
    plt.show()
    print(f"Rectangle saved as {save_filename}")

def draw_parallelogram(a: float, b: float, angle_deg: float, color: str = "green", annotation: str = "", save_filename: str = "parallelogram.png"):
    """
    Draw a parallelogram given sides a, b and the angle (in degrees) between them.
    The drawn figure is annotated with the provided text.
    
    Parameters:
        a (float): Length of side a.
        b (float): Length of side b.
        angle_deg (float): Angle in degrees between sides.
        color (str): Color for the parallelogram.
        annotation (str): Text annotation to display on the figure.
        save_filename (str): Filename for saving the image.
    """
    angle_rad = math.radians(angle_deg)
    # Calculate vertices, starting from (0, 0)
    x0, y0 = 0, 0
    x1, y1 = a, 0
    x2, y2 = a + b * math.cos(angle_rad), b * math.sin(angle_rad)
    x3, y3 = b * math.cos(angle_rad), b * math.sin(angle_rad)
    
    fig, ax = plt.subplots()
    polygon = patches.Polygon([[x0, y0], [x1, y1], [x2, y2], [x3, y3]], closed=True,
                              edgecolor='black', facecolor=color)
    ax.add_patch(polygon)
    
    xs = [x0, x1, x2, x3]
    ys = [y0, y1, y2, y3]
    ax.set_xlim(min(xs)-1, max(xs)+1)
    ax.set_ylim(min(ys)-1, max(ys)+1)
    ax.set_aspect('equal')
    
    plt.title(f"Parallelogram: a={a}, b={b}, angle={angle_deg}°")
    
    # Compute the centroid to position the annotation.
    centroid_x = sum(xs) / 4
    centroid_y = sum(ys) / 4
    if annotation:
        plt.text(centroid_x, centroid_y, annotation, fontsize=12, color='black',
                 ha="center", va="center", bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))
    
    plt.savefig(save_filename)
    plt.show()
    print(f"Parallelogram saved as {save_filename}")

def run_assignment():
    """
    Interactive function to test drawing of geometric figures.
    The user is prompted for the figure type, dimensions, color, and annotation text.
    Based on the input, the function draws and saves the corresponding figure.
    """
    print("Select figure to draw:")
    print("1. Rectangle")
    print("2. Parallelogram")
    
    while True:
        try:
            choice = int(input("Enter your choice (1 or 2): "))
            if choice in [1, 2]:
                break
            else:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    if choice == 1:
        # Input parameters for rectangle.
        try:
            width = float(input("Enter rectangle width: "))
            height = float(input("Enter rectangle height: "))
            color = input("Enter rectangle color (e.g., blue): ")
            annotation = input("Enter annotation text for the rectangle: ")
        except ValueError:
            print("Invalid dimensions entered.")
            return
        rect = Rectangle(width, height, color)
        print(f"\n{rect}")
        draw_rectangle(rect, annotation=annotation)
    else:
        # Input parameters for parallelogram.
        try:
            a = float(input("Enter side a for parallelogram: "))
            b = float(input("Enter side b for parallelogram: "))
            angle = float(input("Enter the angle (in degrees) between sides: "))
            color = input("Enter parallelogram color (e.g., green): ")
            annotation = input("Enter annotation text for the parallelogram: ")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return
        draw_parallelogram(a, b, angle, color=color, annotation=annotation)

if __name__ == "__main__":
    run_assignment()
