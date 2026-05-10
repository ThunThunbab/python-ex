#Challenge 1: Smart Greeting System
#Question: Write a program that asks the user for their name and age.
#Convert the name to uppercase.
#If age is less than 13 → print "You are a kid!"
#Otherwise → print "Welcome!"
#Always print: "HELLO, [NAME]" at the end.

name = input('What is your name?')
age = int(input('What is your age?'))
name_f = name.upper()
if age < 13 :
  print('You are a kid.')
else:
  print('welcome')
print(f'HELLO,{name_f}.')
