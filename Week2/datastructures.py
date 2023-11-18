Data1 = [7, False, "Apple", True, 7, 98.6]

# Task 1: Count the number of items
count_items_data1 = len(Data1)
print("Number of items in Data1:", count_items_data1)

# Task 2: Find the value of the fourth item stored in the data set
fourth_item_data1 = Data1[3]
print("Value of the fourth item in Data1:", fourth_item_data1)

# Task 3: Count the number of times 7 appears
count_seven_data1 = Data1.count(7)
print("Number of times 7 appears in Data1:", count_seven_data1)

# Data Set 2
Data2 = ["July", 4, 8, "Tango", 4.3, "Bingo"]

# Task 4: Remove a random element from the data set
import random
random_element = random.choice(Data2)
Data2.remove(random_element)
print("Data2 after removing a random element:", Data2)

# Task 5: Add "Alpha" to the data set
Data2.append("Alpha")
print("Data2 after adding 'Alpha':", Data2)

# Task 6: Print data set
print("Data2:", Data2)

# Data Set 3
Data3 = ["A", 7, -1, 3.14, True, 7]

# Task 7: Print the data set in reverse order
reverse_data3 = list(reversed(Data3))
print("Data3 in reverse order:", reverse_data3)

# Task 8: Change the second value in the data set to ‘B’
Data3[1] = 'B'
print("Data3 after changing the second value to 'B':", Data3)

# Task 9: Remove the last item and print the data set
removed_item_data3 = Data3.pop()
print("Data3 after removing the last item:", Data3)

# Data Set 4
Data4 = {"name": "Joe", "age": 26, "active": True, "hourly_wage": 14.75}

# Task 10: Change "active" to False
Data4["active"] = False

# Task 11: Add "address" with a value of "123 West Main Street"
Data4["address"] = "123 West Main Street"

# Task 12: Print the weekly salary for Joe if he worked a full 40 hour week
weekly_salary_joe = Data4["hourly_wage"] * 40
print("Weekly salary for Joe:", weekly_salary_joe)

# Task 13: Print the data set
print("Data4:", Data4)
