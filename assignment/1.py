#Question 1.
#Write a program to GET random data of an user and write it in a File named
#users.csv. Each GET request must have an interval time of 1 second and append the
#information in a comma separated format
import csv
import random
import time

header = ['Username', 'Age', 'Country']
filename = 'users.csv'

# Generate random user data
def get_user_data():
    username = 'user' + str(random.randint(1, 10000))
    age = str(random.randint(18, 100))
    country = 'country' + str(random.randint(1, 100))
    return username, age, country

# Write user data to csv file
def write_to_csv(data, header, filename):
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(header)
        writer.writerow(data)

while True:
    user_data = get_user_data()
    write_to_csv(user_data, header, filename)
    time.sleep(1)
