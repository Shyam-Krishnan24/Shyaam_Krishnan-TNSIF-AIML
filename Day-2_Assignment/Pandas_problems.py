# Student Performance DataFrame

import pandas as pd

data = {
    "Name": ["Arun", "Varun", "Rahul", "Karthik", "Priya", "Sneha", "Vijay", "Anu"],
    "Department": ["AI&DS", "CSE", "ECE", "AI&DS", "CSE", "IT", "ECE", "AI&DS"],
    "Marks": [85, 72, 90, 65, 78, 88, 70, 82],
    "Attendance": [90, 75, 95, 78, 85, 92, 70, 88]
}

df = pd.DataFrame(data)

print("First 5 Students:")
print(df.head())

print("\nAverage Marks:", df["Marks"].mean())

print("\nStudents who scored more than 75:")
print(df[df["Marks"] > 75])

print("\nStudents whose attendance is below 80%:")
print(df[df["Attendance"] < 80])

print("\nStudents sorted by Marks:")
print(df.sort_values("Marks"))



# Product Sales Analysis
data = {
    "Product Name": ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 25000, 2000, 1500, 800, 12000],
    "Quantity Sold": [20, 60, 75, 40, 100, 30]
}

df = pd.DataFrame(data)

df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("\n \n \nProduct Sales Data:")
print(df)

highest_sales = df.loc[df["Total Sales"].idxmax()]
print("\nProduct with Highest Sales:")
print(highest_sales)

print("\nAverage Product Price:", df["Price"].mean())

print("\nProducts with Quantity Sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

print("\nProducts Sorted by Total Sales:")
print(df.sort_values("Total Sales"))
