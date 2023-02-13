Random User Data Management
This repository contains code to get random user data, sort the data, and retrieve the details of a user based on their ID or username. The code is written in Python and the data is stored in a CSV file.

Getting Random User Data
The code in the file get_user_data.py sends GET requests to the random user API (https://randomuser.me/api/) with a 1 second interval and writes the retrieved data to a CSV file named users.csv. Each user's information is separated by a comma and a new row is added to the file for each GET request.

To run the code, open a terminal and navigate to the directory containing the code. Then, run the following command:

code:
python get_user_data.py
Sorting User Data
The code in the file sort_user_data.py sorts the data in the users.csv file by the first name and writes the sorted data to a new file named users-sorted.csv.

To run the code, open a terminal and navigate to the directory containing the code. Then, run the following command:

code:
python sort_user_data.py
Retrieving User Details
The code in the file get_user_details.py retrieves the details of a user based on their ID or username. The details are retrieved from the users.csv file.

To run the code, open a terminal and navigate to the directory containing the code. Then, run the following command:


python get_user_details.py
When the code is running, you will be prompted to enter the ID or username of the user. Enter the ID or username and the details of the user will be printed to the terminal. If the user is not found, a message indicating that the user was not found will be printed.

Example Output
Here is an example of the output when running the get_user_details.py code:

yaml

code:
Enter the ID or username: Alice
First name: Alice
Last name: Anderson
Email: alice.anderson@example.com
Gender: Female



