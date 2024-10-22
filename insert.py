from pymongo import MongoClient

client = MongoClient('localhost:27017')

db = client.employeedata

def insert():

try:

eid = input('Enter Employee id :')

ename = input('Enter Name :')

eage = input('Enter age :')

ecountry =input('Enter Country :')

db.employees.insert_one(

{ "eid": eid, "ename":ename, "eage":eage, "ecountry":ecountry })

print("\nInserted data successfully\n")

except Exception:

print(str(e))

insert()