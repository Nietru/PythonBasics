#PYTHON BASICS:

print("Hello, Silly Goose!")
print("You honk loudly.")

#Variable = A reuable container for a value (string, integer, float, boolean)

full_name = "Tifannie Truman"
age = 36
gpa = 3.2
#booleans are either True or False.
is_student = False

print(f"Hello, {full_name}. You are {age} years old.")
print(f"Your GPA is {gpa}.")

if is_student:
    print("You are a student.") 
else:
    print("You are not a student.")

# ARITHMETIC = 
    # + addition, 
    # - subtraction, 
    # * multiplication, 
    # / division (returns a float), 
    # // division (returns an integer), 
    # ** exponent,
    #  % modulo (returns the remainder)

friends = 5

friends += 1 # makes friends = 6

friends *= 2 # makes friends = 12

friends /= 5 # makes friends = 2.4
remaining_friends = friends % 2  # makes remaining_friends = 2.4 % 2 = 0.4    te modulus operator returns the remainder of a division

print(friends)
print(remaining_friends)

# TYPECASTING - The process of converting a value from one data type to another - str(), int(), float(), bool()

name = "Amanda"
age = 25
gpa = 2.8
is_enrolled = True

print(gpa)
print(type(gpa))  # prints <data type 'float'>

gpa = int(gpa)  # converts gpa from a float to an integer, truncating the decimal part
print(gpa)

print(type(gpa))  # prints <data type 'int'>

age = str(age)  # converts age from an integer to a string
#age += 1     # This will cause an error because you cannot concatenate a string and an integer
age += "1"  # This will concatenate the string "1" to the string representation of age making it 251 instead of 25
print(age)
print(type(age))  # prints <data type 'str'>

name = bool(name)  # converts name from a string to a boolean. Non-empty strings are True, empty strings are False
print(name)
print(type(name))  # prints <data type 'bool'>

# Making the name a boolean can be useful to check if a user has entered their name. 
# It will return false if empty and remind the user to enter their name. Once they enter their name they can proceed to the next step in the program.


# INPUT - The input() function allows user input. It always returns a string, so you may need to typecast it to another data type.

full_name = input("Enter your name: ")
my_age = int(input("Enter your age: "))

print(type(my_age))  # prints <data type 'str'> because input() always returns a string    

print(full_name)
print(f"Hello, {full_name}. You are {my_age} years old.")

# IF-STATEMENTS - A block of code that will execute if a condition is true. If the condition is false, the block of code will not execute.
# (if, elif, else) - if a condition is true, execute this block of code. If the condition is false, check the next condition. If none of the conditions are true, execute the else block.

has_ticket = True
price = int(10.00)

if my_age >= 18:
    print("You are an adult.") # the order does matter. If you put the elif statement first, it will never be reached because the if statement will always be true for ages 18 and up.
    print(f"The price for an adult ticket is ${price:.2f}.") #.2f formats the price to 2 decimal places. The space before the .2f is to add a space before the dollar sign for positive numbers.
                                                                #  If you want to remove the space, just remove the space before the .2f.
elif my_age >= 13:
    print("You are a teenager.")
    print(f"The price for a teenager ticket is ${price:.2f}.")
elif my_age == 0:    # you have to use == to check for equality. A single = is used for variable assignment.
    print("You were just born.")    
else:
    print("You are a child.")
    print(f"The price for a child ticket is ${price * 0.5:.2f}.")

if has_ticket:
    print("You can enter the concert. You have a ticket.")
else:
    print("You cannot enter the concert. You do not have a ticket.")


# LOGICAL OPERATORS - Used to combine conditional statements. (and, or, not)
# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Returns True if the statement is false (inverts the boolean value of the statement)

temp = int(input("Enter the temperature (celcius): "))
is_raining = True
is_sunny = True

if temp > 35 or temp < 3 or is_raining:   # with "or", if any of the conditions are true, the block of code will execute.
    print("The weather is bad. The event is cancelled.")
elif temp > 34 and is_sunny:  # with "and", both conditions must be true for the block of code to execute.
    print("The weather is too hot! 🌡️  The event is cancelled.")
elif 2 > temp and not is_sunny:     # line wont execute because of if-statement line 116, but this is how you would use the "not" operator to invert the boolean value of is_sunny.
    print("The weather is too cold! ❄️  The event is cancelled.")
else:
    print("The weather is good. The event is on.")


# WHILE LOOPS - A block of code that will execute as long as a condition is true. If the condition is false, the block of code will not execute.
# we recheck the condition after each iteration of the loop. If the condition is still true, the loop will continue to execute. If the condition is false, the loop will stop executing.
# really great for user input validation. You can use a while loop to keep asking the user for input until they enter a valid value.

if 1 == 1:
    print("I am stuck in a loop")  # if statement will only execute once because the condition is only checked once. The loop will not continue to execute because there is no loop.

#hile 1 == 1:
    #print("I am stuck in a loop")  # this will print "I am stuck in a loop" forever because the condition is always true. You can stop the loop by pressing Ctrl + C in the terminal.

the_name = input("Enter your name: ")

while the_name == "":  # the while loop checks if the name field is empty. It will not execute at all if the user enters their name. 
    the_name = input("Enter your name: ")

the_age = int(input("Enter your age: "))

while the_age <= 0:  # the while loop checks if the age is less than or equal to 0. It will not execute at all if the user enters a valid age. 
    the_age = int(input("Enter your age: "))

print(f"Hello, {the_name}. You entered your name correctly.")
print(f"You are {the_age} years old.")


# FOR LOOPS - A block of code that will execute a specific number of times.  (str, list, tuple, set)If the condition is false, the block of code will not execute.

for i in range(10):  # range(10) generates a sequence of numbers from 0 to 9. The loop will execute 10 times. The variable i is the loop counter. 
                     # It will start at 0 and increment by 1 each time the loop executes.
                     # "i" is short for "index" or "iterator". It is a common convention to use i as the loop counter variable name. 
                     # you can use any variable name you want, but using i is a common convention. You can also use j, k, l, m, n, etc. for nested loops.
    print(i)    

for i in range(91, 101):  # range(91, 101) generates a sequence of numbers from 91 to 100 (first number is inclusive and second number is exclusive, thats why it stops at 100).
    print(i)    

for i in range (1, 11, 2):  # will increment by 2 each time the loop executes. The third parameter in range() is the step value.
    print(i)    

some_name = "Tifannie Truman"

for letter in some_name:
    print(letter, end = "~") # inserts "~" between each letter instead of a new line. 
                            #The end parameter in print() specifies what to print at the end of the output. 
                            # The default value is "\n" which is a new line character. You can change it to any string you want.

# THIS FILE IS GETTING LONG AND WANT TO REUSE VARIABLES WITHOUT COMMENTING OUT THE CODE ABOVE, SO I WILL CREATE A NEW FILE FOR THE NEXT SECTION OF CODE. "pythonfile2.py"

