#Passing a funtion to a list

def count_name_lengths(nusers):
    more_than_five = 0
    five_or_less = 0
    
    for name in users:
        if len(name) > 5:
            more_than_five += 1
        else:
            five_or_less += 1
    
    return more_than_five, five_or_less
# Example list of 10 names
users = ["John", "Sameen", "Lionel", "Groves", "Zoe", "Harold", "Jocelyn", "Lee", "Calvin", "Elias"]
# Call the function
more, less_or_equal = count_name_lengths(users)
print(f"Users with names longer than 5 letters: {more}")
print(f"Users with names equal to or fewer than 5 letters: {less_or_equal}")

#Lists in Python

numbers = [20, 16, 30, 2, 25]
print("Original list:", numbers)
# Sort the list
numbers.sort()
print("Sorted list:", numbers)
#Print the first and last elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])
#Add a new number
numbers.append(40)
#Remove a number (say 30)
numbers.remove(30)
#Print updated list
print("Updated list:", numbers)

#Variables

name = "Sameen Omar"
age = 25
country = "Turkey"
print(f"My name is {name}, I am {age} years old, and I live in {country}")

#Dictionaries

Student = {"name": "Celine Oman", "age": 19, "course": "Computer Science"}
print(Student)
# Adding a new key-value pair
Student["grade"] = "A"
print(Student)
# Updating an existing key-value pair
Student["age"] = 20
print(Student)
# Deleting a key-value pair
del Student["course"]
print(Student)
# accessing data in a dictionary
User = {"username": "sameen", "email": "sameen@example.com", "location": "Abu Dhabi"}
print(User["email"])
print(User.get("location"))
# Iterate over a dictionary
Prices = {"Apples": 300, "Bananas": 900, "Oranges": 150}
for fruit, price in Prices.items():
    print(f"{fruit} cost NGN{price} for each")
# Creating a discounted dictionary for 10% off each item
discounted_prices = {fruit: price * 0.9 for fruit, price in Prices.items()}
print(discounted_prices)
# Nested dictionaries
Users = {
    "user1": {"username": "sameen", "email": "sameen@example.com", "location": "Abu Dhabi", "age": 25},
    "user2": {"username": "john", "email": "john@example.com", "location": "New York", "age": 30},
    "user3": {"username": "harold", "email": "harold@example.com", "location": "London", "age": 34}
}
print(Users["user1"]["email"])
print(Users["user2"].get("location"))
Users["user4"] = {"username": "zoe", "email": "zoe@example.com", "location": "Washington DC", "age": 28}
print(Users["user4"]["email"])
# creating new dictionary from two lists
names = ["sameen", "john", "harold", "zoe"]
occupation = ["doctor", "security consultant", "programmer", "private investigator"]
new_users = {name: occ for name, occ in zip(names, occupation)}
print(new_users)

#For loop
for i in range(1, 21, 3):
    if i%2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

#While loop
i = 1
while i<=5:
    print("Machine Learning Task")
    i += 1
