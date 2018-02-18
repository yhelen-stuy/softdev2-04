from pymongo import MongoClient
import random
import json

pokemon = ""

c = MongoClient('lisa.stuy.edu')

db = c['HYE_Jay-Z']
coll = db['pokemong']

'''
We used the pokedex dataset, which contains the 151 Gen I pokemon, with their
name, pokedex number, and information about them, such as their type, spawn
chance, and evolutions.
The dataset can be found here:
    https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json

To import this data, we noticed that the pokemon in the json file were all
in a list of dictionaries, the value of the first key in the dictionary, 'pokemon'.
As a list of dictionaries was what we wanted to import the data into mongo,
we just used insert_many on the value of that key to produce our db.
'''
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
        print

def find_pokemong(pokemong):
    return coll.find({"name": pokemong})

def find_id(idd):
    return coll.find({"id": idd})

#returns all pokemon with that type (even if it has another one as well)
def find_type(typee):
    return coll.find({"type": typee})

#returns w/ spawn chance greater than given spawn
def find_type_and_spawn(typee, spawn):
    return coll.find({"type": typee, "spawn_chance": {"$gt": spawn}})

def find_next_evo(next_evo):
    return coll.find({"next_evolution.name": next_evo})

def find_fun(typee):
    pokes = coll.find({"type": typee})
    return pokes[random.randint(0, pokes.count() - 1)]

print "===MEW==="
print_cursor(find_pokemong("Mew"))
print "===POKE #1==="
print_cursor(find_id(1))
print "===FIRE==="
print_cursor(find_type("Fire"))
print "===FIRE & SPAWN > .5==="
print_cursor(find_type_and_spawn("Fire", 0.50))
print "===EVOLVES TO VENUSAUR==="
print_cursor(find_next_evo("Venusaur"))
print "===RANDOM FIRE==="
print find_fun("Fire")


