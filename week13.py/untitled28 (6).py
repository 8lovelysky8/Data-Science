# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fC2JkDKpRonmPu0q3jNaSJeELvfulu4o
"""

def get_bmi(height, weight):
    """
    Calculate BMI based on height and weight
    """
    height = height / 100
    bmi = weight / height**2
    return bmi