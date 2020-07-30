"""
Author: FaDr_YL (_YL_)
"""


str_input = input("Input something: ")
print("Your input: " + str_input)

print("\n-----\n")

file = open("hello_world.txt", "r")
print(file.read())
file.close()

print("\n-----\n")

file = open("hello_world.txt", "r")
print(file.read(3))
file.close()

print("\n-----\n")

file = open("hello_world.txt", "r")
content = ""
for line in file:
    content += line
print(content)
file.close()

