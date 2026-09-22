# @author: Ntobeko Makakhathi
# date: 2026-09-22
# description: practing python code for database to python conversion

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uzumaki16*",
    database="africansafaridb"
)
name = input("Enter your name: ")
mycursor = mydb.cursor()
mycursor.execute(f"SELECT * FROM user where FirstName = '{name}'")
result = mycursor.fetchall()
if result:
    for db in result:
        print(f"Customer number: {db[0]}, \nFirst Name: {db[1]}, \nLast Name: {db[2]}, \nPhysical Address: \n\t{db[3]},\n\t{db[4]},\n\t{db[5]},\n\t{db[6]},\n\t{db[7]}, \nDate of Birth: {db[8]}")
else:
    print("No user found with that name.")

print("Thank you for using our service.")