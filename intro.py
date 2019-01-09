# Output to the terminal
print("hello, world")

# not an array, but close!
my_list = ['Fred', 3, True, 'hello', 345, None, 'bye', 'more stuff', 45]

# delete
del(my_list[5])
print("mylist minus one thing", my_list)

# length
print("length of list", len(my_list))

# works on strings, too
name = "Fred"
print("name length", len(name))

# slicing gives you the first index up to the last index
print(my_list[2:5])

# make a clean copy of a list that does not point to the original list in memory
your_list = my_list[:]
print(your_list)

# This does not create a separate list. It's just a pointer to the same list with a new variable name
your_list = my_list
del(your_list[2])
# print( "My list changed?", my_list) # yup, it did change. Eek

# Add something at a specific index
my_list.insert(0, "Blah")
# print(my_list)

# A dictionary is a collection of key/value pairs
person = {
  "name": "Fred",
  "age": 24,
  45: "wtf"
}

# No dot syntax here. Gotta use brackets
person["phone"] = 3455678

# Same for setting a new value
person["address"] = {"street": "123 Sesame St", "zip": 12345}
# print("person", person["address"]["street"])

# A tuple is immutable ( Can't add or delete anything from it)
zoo = ("dog", "monkey", "chicken", "bird", "cuttlefish")
print(zoo)
print(zoo[3])

# But you can change it to a list if you want to!
zoo_list = list(zoo)
print(zoo_list)

# Then we can add stuff to it
zoo_list.append("fish")

# Reassign the value of zoo back to a tuple
zoo = tuple(zoo_list)
# print("new zoo for you", zoo)

# sets are unique
new_set = {} # Oops. Makes a dictionary! Must use my_set = set() for creating an empty set
my_set = {"foo", "bar", "foo"} # This creates a set, no problem, since you added values to it as you created it

# Add one thing
my_set.add("monkey")

# add multiple things
my_set.update({"baz bazoo", "hello", "345"})
print(my_set)

# no implicit coercion! Gotta do this to avoid throeing an error
print( "4" + str(3))
print( int("4") + 3)

# if else statements
cow = "moo"
dog = "woof"
if cow == "moo" and dog == "woof":
  print(cow)
elif cow == "Woof":
  print("WTF?")
else:
  print("The end")

# Looping through any collection
for thing in my_set:
  print(thing.title())

# Nested loops
for item in my_list:
  for animal in zoo:
    print("I like to take my {0} to see the {1} at the zoo".format(item, animal))

# like a regular loop, gives you the key
# for trait in person.keys():
#   print(trait)

# gives you the value
# for trait in person.values():
#   print(trait)

# both key and value
# for key, trait in person.items():
#   print(key, trait)
# =====

# joins!
list_of_stuff = ["stuff", "things", "junk", "candy bar"]
print( (" ... ").join(list_of_stuff))

# JS way
# list_of_stuff.join(" ... ")
# ====

# functions
def do_something(bar="tree", foo="monkeys"):
  if foo == "monkeys":
    print("I like " + foo + bar)
    return
  print("Something else " + foo)

# *named* parameter position isn't important AS LONG AS it comes after the positional arg of `myList`.
do_something("tree", foo="dogs")
# do_something()

# =====
# scope

name = "fred"

def sayName():
  name = "Sally"
  print("inside name", name)

def sayName():
  global name
  name = "Sally"
  print("inside name", name)

sayName()
print("outside name", name)

if __name__ == '__main__':
  print("This is a file run directly!")
