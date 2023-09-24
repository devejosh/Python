#Using string and string concatnation.

# This is a very simple program to print, get input and get the length of a string.
print("Basic program to get the length of a name in python \n")

name = input ("What is your name :")

#Getting the length of the name through len() function

length = len (name)
print ("Hello " + name + ", Your name is " + str(length) + " characters long")