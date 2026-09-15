# Student Marks Analysis
import numpy as np

arr=np.array([45,50,55,60,77,45,80,91,71,84])

total=np.sum(arr)
avg=np.mean(arr)
max_num=np.max(arr)
min_num=np.min(arr)
greater_than_75=arr[arr>75]

print(f"Marks: {arr}")
print(f"Total Marks: {total}")
print(f"Average Marks: {avg}")
print(f"The maximum number {max_num}")
print(f"The minimum number {min_num}")
print(f"The number greater than 75 {greater_than_75}")


# Temperature Analysis

temperature = np.array([28, 32, 30, 35, 29, 31, 27])
average = np.mean(temperature)
highest = np.max(temperature)
lowest = np.min(temperature)
above_30=temperature[temperature>30]
upd_temp=temperature+2

print("\n\nTemperatures:", temperature)
print("Average Temperature:", average)
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)
print(f"The number greater than 30 {above_30}")
print("The updated temperature is",upd_temp)
