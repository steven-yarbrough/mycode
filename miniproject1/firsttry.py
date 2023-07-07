#!/usr/bin/env python3


#checks if the number the user enter  is out of the designanted number range of 1-15
number = int(input("Enter a number between 1 and 15: "))
#if number is out of scope 1-15 print smart as$ comment
if number < 1 or number > 15:
    print("Did you even read the question, fool?")
elif number % 2 == 0:  
    print(number, "is even, look at you go! My little crayon eater is all grown up!.")
else:
    print(number, "is odd, thats ok, God Loves Ugly.")
