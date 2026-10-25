# Happy new year forloop:

import time  #import the time module to use the sleep() function to pause the program for a specific amount of time.

for i in range (10, 0, -1):  # will decrement by 1 each time the loop executes. 
                            # The third parameter in range() is the step value. (zero is exclusive, so it will stop at 1)
    print(i)
    time.sleep(1)  # will pause the program for 1 second before executing the next line of code. (the parameter is in seconds)

print("Happy New Year! 🎉")