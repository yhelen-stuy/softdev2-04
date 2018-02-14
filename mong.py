from pymongo import MongoClient


c = MongoClient('lisa.stuy.edu')


db = c['test']
coll = db['restaurants']



def find_borough(borough):
    for rest in coll.find({"borough": borough}):
        print rest

def find_zip(zipp):
    for rest in coll.find({"address.zipcode": str(zipp)}):
        print rest

def find_zip_and_grade(zipp, grade):
    for rest in coll.find({"address.zipcode": str(zipp), "grades.grade": grade}):
        print rest

def find_zip_and_score_below(zipp, score):
    for rest in coll.find("stuff"):
        print rest

#find_borough("Queens")
find_zip(11365)
find_zip_and_grade(11365, "A")
