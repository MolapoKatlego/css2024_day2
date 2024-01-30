# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 18:29:11 2024

@author: Katlego Molapo
"""

"""
1. Lists
2. Dictionaries
3. Data Frame - Specific to panda

"""

import pandas
file = pandas.read_csv("country_data.csv")
print(file)

age1 = 30
age2 = 25
age3 = 29

age = [30,25,29,46,22,3.14]
print(age)

print(age[0])

print(age[1])

print(min(age))

print(max(age))

print(sum(age))

print(len(age))

average = sum(age)/len(age)
print(average) 

age = [30,25,29,46,22,3.14]
age.append(100)
print(age)

#storing text

g1 = "M"
g2 = "F"
g3 = "M"
gender = ["M", "F", "M"]

print(g1)
print(g2)
print(g3)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

# country list
country = ["South Africa","Botswana","Kenya","Egypt"]
print(country)
print(country[0])
print(country[3])



"""
LISTS
"""
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])



"""
DICTIONARIES
"""
Mammals = {"cat" : "A cute animal", "Lion": "King of the jungle"," Elephant":"A giantic herbivore"
          }
print(Mammals["cat"])


"""
Data Frame
"""

Fruits = [ "apple"," Banana", "Orange", "Grape", "Kiwi"]
Size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]
Fruit_size = {"fruits": Fruits, "Sizes":Size_nm}

"""
df = dataframe
"""
df = pandas.DataFrame(Fruit_size)
print(df)


# Accessing specific columns
print(df['fruits'])
print(df['Sizes'])

# Basic statistics
print(df['Sizes'])
print(df['Sizes'])
print(df['Sizes'])

# Filtering data
print (df.describe())
print(df[df['Sizes']>10])

# Slicing rows and columns
print(df[1:3])

# Adding a new column
prices=[10, 12.5, 16, 23, 7]
df['prices']= prices
print(df)


# Removing a column
df.drop(columns=['Sizes'], inplace=True)
print(df)