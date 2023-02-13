#Question B.
# Write a program to Input Id or Username of an user and return the details of
#that user in the output of the program

import csv

def read_csv(filename):
    users = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append(row)
    return users

def find_user(id_or_username, users):
    for user in users:
        if user['Id'] == id_or_username or user['Username'] == id_or_username:
            return user
    return None

filename = 'users.csv'
users = read_csv(filename)

id_or_username = input("Enter Id or Username: ")
user = find_user(id_or_username, users)

if user is None:
    print("User not found.")
else:
    print("First Name:", user['First Name'])
    print("Last Name:", user['Last Name'])
    print("Username:", user['Username'])
    print("Id:", user['Id'])
