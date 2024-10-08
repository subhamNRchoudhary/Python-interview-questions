# -*- coding: utf-8 -*-
"""Part 5 - 8 Python Important Questions for Interview

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nGNWRE_3MeYGwTRshUZTg3-I-OQlaA6R

**1. Tuple and Set**
"""

a_Tuple = (1,2,3,4,9)

b_set = {1,2,3,4,9}

print("Tuple:",a_Tuple)
print("Set:",b_set)

"""**2. a = 'hloo', b = " ".join(a), print(b)**"""

a = 'SubhamChoudhary'
b = " ".join(a)
print(b)

"""**3. Create a Pandas DataFrame**"""

import pandas as pd

Data = {'Name': ['a', 'b', 'c', 'd'], #  DataFrame
        'Age': [28, 24, 35, 32],      #  DataFrame
        'City': ['Bihar', 'Karnataka', 'Delhi', 'WB']}  #  DataFrame

hi = pd.DataFrame(Data)
print(hi)

"""**4. How to remove a blank column in Python using the drop function**"""

import pandas as pd

Data = {'Name': ['a', 'b', 'c', 'd'], #  DataFrame
        'Age': [28, 24, 35, 32],      #  DataFrame
        'City': ['Bihar', 'Karnataka', 'Delhi', 'WB'], #  DataFrame
        'Empty': ['']*4}

hi = pd.DataFrame(Data)
print("Before removing the blank column:")
print(hi)

hi.drop(columns=['Empty'], inplace=True) # Removing

print("\nAfter removing the blank column:")
print(hi)

"""**5. Find the average of a given list of numbers without using an inbuilt function**"""

def find_average(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    average = total_sum / len(numbers)
    return average

numbers = [10, 20, 30, 40, 50]
avg = find_average(numbers)
print("Average:", avg)

"""**6. When to use inplace=True in Python**

*inplace=True is used when you want to modify the data in place, meaning the original data structure is modified without creating a new one. For example, in a DataFrame, using inplace=True will modify the original DataFrame directly.*
"""

import pandas as pd

data = {'Name': ['a', 'b', 'c', 'd'],
        'Age': [28, 24, 35, 32]}

df = pd.DataFrame(data)
print("Before modification:")
print(df)

df.drop(columns=['Age'], inplace=True) # Using inplace=True

print("\nAfter modification:")
print(df)

"""**7. Add the last 2 digits of a number**"""

def add_last_two_digits(number):
    last_digit = number % 10
    second_last_digit = (number // 10) % 10
    return last_digit + second_last_digit

number = 12345
result = add_last_two_digits(number)
print("Sum of last:", result)

"""**8. Count the common digits between two numbers**"""

def count_common_digits(num1, num2):
    digits_num1 = set(str(num1))
    digits_num2 = set(str(num2))
    common_digits = digits_num1.intersection(digits_num2)
    return len(common_digits)

num1 = 12345
num2 = 54321
common_count = count_common_digits(num1, num2)
print("Count of common digits:", common_count)