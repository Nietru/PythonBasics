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

for fruit in fruits:  # iterates through each element in the list and assigns it to the variable fruit
    print (fruit)     # prints each element in the list on a new line
for fruit in fruits:
    print(fruit, end = " ")  # prints each element in the list, end does a space instead of a new line after each element. (default is "\n" which is a new line character)

#