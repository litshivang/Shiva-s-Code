#Question A.
#Write a program to read users.csv and create users-sorted.csv by applying
#sorting algorithm

import csv
import random
import string

filename = 'users.csv'
sorted_filename = 'users-sorted.csv'

# Read data from csv file into a list of dictionaries
def read_csv(filename):
    users = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            users.append(row)
    return users

# Write list of dictionaries to csv file
def write_csv(users, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=users[0].keys())
        writer.writeheader()
        for user in users:
            writer.writerow(user)

# Generate random user data
def generate_user_data():
    user = {}
    user['First Name'] = ''.join(random.choices(string.ascii_letters, k=10))
    user['Last Name'] = ''.join(random.choices(string.ascii_letters, k=10))
    user['Username'] = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return user

# Generate a list of 10 random users
users = [generate_user_data() for _ in range(10)]

# Write generated user data to csv file
write_csv(users, filename)

# Read data from csv file
users = read_csv(filename)

# Sort data based on username
users = sorted(users, key=lambda x: x['Username'])

# Write sorted data to new csv file
write_csv(users, sorted_filename)
