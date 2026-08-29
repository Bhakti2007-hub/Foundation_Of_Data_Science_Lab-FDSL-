#-------------------WITHOUT USING INBUILT FUNCTION---------------------

import math
 #import data
val = [2,4,6,8,10]

#find minimum

min_val = val[0]
for i in val:
    if i<min_val:
        min_val=i

#find maximum

max_val = val[0]
for i in val:
    if i> max_val:
        max_val = i

#find mean
total=0

for i in val:
    total=total+i
mean=total/len(val)

#find Varience

sum_squared_difference =0

for i in val:
    diff = i - mean
    squared_difference= diff*diff
    sum_squared_difference = sum_squared_difference + squared_difference
variance = sum_squared_difference/len(val)

#find standard deviation
std_dev = math.sqrt(variance)

#find coefficient of variation

coe_var=(std_dev/mean)*100

#display

print("Data:",val)
print("Minimum:", min_val)
print("Maximum:", max_val)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Coefficient of Variation:", coe_var, "%")



#---------------------Using Built in Function-----------------
import pandas as pd
import statistics

# Read dataset
data = pd.read_csv("Salary_Data.csv")

# Select Salary column
val = data["Salary"].dropna()

# Using built-in functions
min_val = min(val)
max_val = max(val)
mean = statistics.mean(val)
variance = statistics.pvariance(val)
std_dev = statistics.pstdev(val)

# Coefficient of Variation
coe_var = (std_dev / mean) * 100

# Display
print("Dataset:")
print(data)

print("\nStatistics for Salary:")

print("Minimum:", min_val)
print("Maximum:", max_val)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Coefficient of Variation:", coe_var, "%")