# LIST [] = mutable, ordered sequence of elements. most flexible(can be changed, can add/remove elements, can have duplicates, can have different data types)
# TUPLE () = immutable, ordered sequence of elements. (cannot be changed, cannot add/remove elements, can have duplicates, can have different data types)
# SET {} = mutable, unordered collection of unique elements. (can be changed, can add/remove elements, cannot have duplicates, can have different data types)

# all similar to arrays in other programming languages.


#LIST 
fruits = ["apple", "banana", "coconut", "orange"]

print(fruits)  # prints the entire list
print(fruits[0])  # prints the first element in the list (index starts at 0)
print(fruits[-1])  # prints the last element in the list (negative index starts at -1)

fruits[3] = "mango" # changes the value of the fourth element in the list from orange to mango
print(fruits)

fruits.append("kiwi")  # adds a new element to the end of the list
print(fruits)

fruits.remove("banana")  # removes the element "banana" from the list
print(fruits)

fruits.pop(0)  # removes first element from the list
print(fruits)

#fruits.clear()  # removes all elements from the list
#print(fruits)

print('\n')  # new line, creates and empty line in the output before the next print statement.

for fruit in fruits:  # iterates through each element in the list and assigns it to the variable fruit
    print (fruit)     # prints each element in the list on a new line
for fruit in fruits:
    print(fruit, end = " ")  # prints each element in the list, end does a space instead of a new line after each element. (default is "\n" which is a new line character)

print('\n')  


#TUPLE - immutable, which means we cannot change the values of the elements in the list.

dogs = ("Pug", "Golden", "Labrador", "Bulldog")  # tuple of dog breeds
print(dogs)

for dog in dogs:  # iterates through each element in the list and assigns it to the variable dog
    print(dog, end = " ")

print('\n') 

people = {"tifaNNie", "Genevieve", "dahlia", "jolene",}  # set of people names (unordered collection of unique elements
                                                        # will change the order of the elements each time the program is run)

people.add("dylan")  # adds a new element to the set
people.remove("jolene")  # removes an element from the set
#people.clear()  # removes all elements from the set

print(people)  # prints the entire set, and converts the set to lowercase to make the search case-insensitive.

person = input("Enter name to search for: ").lower()
lowercase_set = {person.lower() for person in people}  # creates a new set with all elements in lowercase, that way user input will match regarless of case. (case-insensitive search)

# sets are best for membership testing, which means checking if an element is in the set or not. (faster than lists and tuples)

if person in lowercase_set:  # checks if the element "(user chosen name)" is in the set
    print(f"{person} already exists.")
else:
    print(f"{person} does NOT exist.")
