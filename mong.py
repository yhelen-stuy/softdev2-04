from pymongo import MongoClient
import random
c = MongoClient('lisa.stuy.edu')

db = c['test']
coll = db['restaurants']

# Returns a cursor with all restaurants in borough inputted
def find_borough(borough):
    return coll.find({"borough": borough})

# Returns a cursor with all restaurants in zipcode inputted
# Zipcode can be either string or int
def find_zip(zipp):
    return coll.find({"address.zipcode": str(zipp)})

# Returns a cursor with all restaurants in zipcode inputted and grade specified
def find_zip_and_grade(zipp, grade):
    return coll.find({"address.zipcode": str(zipp), "grades.grade": grade})

# Returns a cursor with all restaurants in zipcode inputted and a score lower than the one inputted
def find_zip_and_score_below(zipp, score):
    return coll.find({"address.zipcode": str(zipp), "grades.score": {"$lt": score} })

# Returns a random restaurant with a zipcode 10 less than the zipcode inputted
def find_fun(zipp):
    rest =  coll.find({"address.zipcode": str(zipp - 10)})
    return rest[random.randint(0, rest.count() - 1)]

# Prints the cursor
def print_cursor(cursor):
    for item in cursor:
        print item

print_cursor(find_borough("Manhattan"))
print_cursor(find_zip(10282))
print_cursor(find_zip_and_grade(10282, "A"))
print_cursor(find_zip_and_score_below(10282, 20))
print find_fun(11372)
