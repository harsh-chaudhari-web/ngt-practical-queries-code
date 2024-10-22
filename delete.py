from pymongo import MongoClient client = MongoClient('localhost:27017')

db = client.employeedata

def delete():

try:

criteria = input("\nEnter employee name to delete\n")

db.employees.delete_many({"ename": criteria})

print("\nDeletion successful\n")

except (Exception):

print(str(e))

delete()