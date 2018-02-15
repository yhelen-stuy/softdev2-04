from pymongo import MongoClient
import random
import json

pokemon = ""

c = MongoClient('lisa.stuy.edu')

db = c['HYE_Jay-Z']
coll = db['pokemong']

#initializes db
def init_db():
    f = open("pokedex.json", "rU")
    pokemong = json.loads(f.read())
    f.close()

    
    pokemon = pokemong["pokemon"]
    coll.insert_many(pokemon)

#init_db()

# Prints the cursor
def print_cursor(cursor):
    for item in cursor:
        print item



def find_pokemong(pokemong):
    return coll.find({"name": pokemong})

def find_id(idd):
    return coll.find({"id": idd})

#returns all pokemon with that type (even if it has another one as well)
def find_type(typee):
    return coll.find({"type": typee})

#returns w/ spawn chance greater than given spawn
#spawn has to be b/w 0 and 1
def find_type_and_spawn(typee, spawn):
    return coll.find({"type": typee, "spawn_chance": {"$gt": spawn}})

def find_next_evo(next_evo):
    return coll.find({"next_evolution.name": next_evo})


#print_cursor(find_pokemong("Mew"))
#print_cursor(find_id(1))
#print_cursor(find_type("Fire"))
#print_cursor(find_type_and_spawn("Fire", 0.50))
print_cursor(find_next_evo("Venusaur"))


