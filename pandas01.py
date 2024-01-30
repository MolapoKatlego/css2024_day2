# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:57:21 2024

@author: Katlego Molapo
"""

"""
Download "data_01.zip" folder found in "Week 1" section.
Unzip it. You will find the a file called "country_data.csv"
put this file in your project folder in Spyder.

"""
import pandas

file = pandas.read_csv("country_data.csv")

print(file)

"""
This is a really useful feature of Pandas as it summarizes 
for you table. It tells you the amount of columns, their names, 
Non-Null Count, and the Dtype or data type.

"""
print(file.info())


"""
The describe() method is used to generate descriptive statistics
of a DataFrame or Series.
It provides a summary of the central tendency, dispersion
and shape of the distribution of a dataset.
It is primarily designed for summarizing numerical data, and it 
provides statistics that are meaningful for quantitative variables.

"""
print(file.describe())
file = pandas.read_csv("iris.csv")

print(file)

file = pandas.read_csv("insurance_data.csv",skiprows=5)

print(file)

file = pandas.read_csv("housing_data.csv")

print(file)


"""
Python Browser Option
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)
