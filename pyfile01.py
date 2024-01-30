# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:41:25 2024

@author: Katlego Molapo
"""

"""
1. Python Scripts
"""
print("My First Python File")




"""
2. Variables
"""
density = 1000

density = 900

mass_kg = 50

"""
1. int - integer - whole number
2. float - number with decimals
3. strings - letters, texts, words, paragraphs
"""

gravity_m_2_sec = 9.8 

water_level_m_above_sea_level = 14.89

pi = 3.14

fruit = "banana"

element = "Potassium"

parasite = "plasmodium"

delivered_prematurely = "<6 months, >6 months < 9 months"




"""
3. Reading In fFles With Pandas
"""
import pandas

file = pandas.read_csv("country_data.csv")

print(file)
print(file.info())
print(file.describe())


file = pandas.read_csv("iris.csv")

print(file)

file = pandas.read_csv("insurance_data.csv",skiprows=5)

print(file)

file = pandas.read_csv("housing_data.csv")

print(file)

 

