# @author: Ntobeko Makakhathi
# date: 2026-09-22
# description: practing python code for database to python conversion

import mysql.connector

# Establish a connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uzumaki16*",
    database="africansafaridb"
)

# Create a cursor object to interact with the database
name = input("Enter your name: ")
mycursor = mydb.cursor()
mycursor.execute(f"SELECT * FROM user where FirstName = '{name}'")
result = mycursor.fetchall()

# Display the results
if result:
    for db in result:
        print(f"Customer number: {db[0]}, \nFirst Name: {db[1]}, \nLast Name: {db[2]}, \nPhysical Address: \n\t{db[3]},\n\t{db[4]},\n\t{db[5]},\n\t{db[6]},\n\t{db[7]}, \nDate of Birth: {db[8]}")
else:
    # No records found
    print("No records found for the given name.")

    # Prompt the user to add a new record
    record = input("Would you like to add a new record? (yes/no): ")
    if record.lower() == "yes" or record.lower() == "y":
        # Prompt the user for the new record details
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address_line1 = input("Enter Address Line 1: ")
        address_line2 = input("Enter Address Line 2: ")
        city = input("Enter City: ")
        province = input("Enter Province: ")
        postal_code = input("Enter Postal Code: ")
        date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")

        # Insert the new record into the database
        sql = "INSERT INTO user (FirstName, LastName, Street, Suburb, City, Province, PostalCode, DOB) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (first_name, last_name, address_line1, address_line2, city, province, postal_code, date_of_birth)
        mycursor.execute(sql, val)
        mydb.commit()
        print(f"Record added successfully. Customer number: {mycursor.lastrowid}")


print("Thank you for using our service.")