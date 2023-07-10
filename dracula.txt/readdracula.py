#! usr/bin/env python3


#read in the contents of dracula txt file using() method in Python3
with open('dracula.txt', 'r') as file:
    data = file.read()


#loops over every line in dracula.txt and prints each line
with open('dracula.txt', 'r') as file:
    for line in file:
        print(line)


#Print the number of lines that contain the word vampire in it.
count = 0

with open('dracula.txt', 'r') as file:
    for line in file:
        if 'vampire' in line.lower():
            count += 1

print(f'The number of lines that contain the word "vampire" is: {count}')
