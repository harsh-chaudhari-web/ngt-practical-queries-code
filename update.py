from pymongo import MongoClient client = MongoClient('localhost:27017')

db = client.employeedata

def update():

try:

ename = input("\nEnter name to update\n")

eage = input("\nEnter age to update\n")

ecountry = input("\nEnter country to update\n")

db.employees.update_one(

{"ename": ename},

{"$set": {

"eage":eage,

"ecountry":ecountry

}

}

)

print("\nRecords updated successfully\n")

except Exception:

print(str(e))

update()