from pymongo import MongoClient client = MongoClient('localhost:27017')

db = client.employeedata

def read():

try:

empCol = db.employees.find()

print("\n All data from EmployeeData Database \n")

for emp in empCol:

print(emp)

except Exception:

print(str(e))

read()