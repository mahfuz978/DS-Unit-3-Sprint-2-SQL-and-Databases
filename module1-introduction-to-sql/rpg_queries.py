import sqlite3
conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

print("Q1: How many total Characters are there?")
query1 = '''
select COUNT(name) 
from charactercreator_character;'''
curs.execute(query1)
print(curs.fetchall()[0][0])

# ANS: 302
# """
print("Q2: How many of each specific subclass?")
# cleric
# fighter
# mage
# necromancer
# thief
query1 = """SELECT COUNT(name) FROM charactercreator_character
INNER JOIN charactercreator_cleric on 
character_id = character_ptr_id;"""
curs.execute(query1)
print(curs.fetchall()[0][0])
# ANS: 75

query1 ="""SELECT COUNT(name) FROM charactercreator_character
INNER JOIN charactercreator_fighter on 
character_id = character_ptr_id;"""
curs.execute(query1)
print(curs.fetchall()[0][0])
#Result: 68

query1 = """SELECT count(name) FROM charactercreator_character
INNER JOIN charactercreator_mage on 
character_id = character_ptr_id;"""
curs.execute(query1)
print(curs.fetchall()[0][0])
# Result: 108

query1 = """SELECT COUNT(name) FROM charactercreator_character
INNER JOIN charactercreator_necromancer on 
character_id = mage_ptr_id;"""
curs.execute(query1)
print(curs.fetchall()[0][0])
# Result: 11

query1 = """SELECT COUNT(name) FROM charactercreator_character
INNER JOIN charactercreator_thief on 
character_id = character_ptr_id;"""
curs.execute(query1)
print(curs.fetchall()[0][0])
# Result: 51

print("Q:3 How many total Items?")
query1 = """select COUNT(name) 
from armory_item;"""
curs.execute(query1)
print(curs.fetchall()[0][0])
# ANS : 174


print ("Q:4 How many of the Items are weapons? How many are not?")
query1 = """select COUNT(name) FROM armory_item
inner JOIN armory_weapon
on item_id   = item_ptr_id;"""
curs.execute(query1)
print(curs.fetchall()[0][0])
# Result: 37 items are weapons
total_ai = 174
weapons = 37
print("There are", (total_ai - weapons) , "items that are not weapons.")

print("Q:5 How many Items does each character have? (Return first 20 rows)")
query1 = """SELECT COUNT(item_id) FROM
charactercreator_character_inventory
GROUP BY character_id LIMIT 20;"""
curs.execute(query1)
print(curs.fetchall())


print("Q:6 How many Weapons does each character have? (Return first 20 rows)")
query1 = """SELECT character_id, COUNT(item_ptr_id) FROM
armory_weapon INNER JOIN
charactercreator_character_inventory on
item_ptr_id = item_id
GROUP BY character_id LIMIT 20;"""
curs.execute(query1)
results = curs.fetchall()
for result in results:
    print(f'character number: {result[0]} has {result[1]} weapons')


print('On average, how many Items does each Character have?')
query1 = """SELECT avg(Item_cnt) from
(SELECT character_id, count(*) as Item_cnt 
FROM charactercreator_character_inventory 
GROUP BY character_id) ;"""
curs.execute(query1)
print(curs.fetchall()[0][0])






