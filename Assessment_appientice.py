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

#Q2
coffee = int(input('Number of coffee'))
cakes = int(input('Number of cakes'))
cake_subt = 30*cakes
cof_subt = 50*coffee
total = cof_subt+cake_subt

if total > 200:
  DP = total*0.1
  total = total - DP
print(f'Your order is {total} baht. ')








#Challenge 4: Username & Password Checker

U = input('What is the user name?')
P = int(input('What is the passcode?'))

if U == 'admin':
  if P == 1234:
    print('Welcome admin!!')
  else:
    print('Error!!!!!')
else:
  print("Error!!!!!!!!")



#Challenge 5: Mini Profile Generator
print('THIS IS NOT A SCAM')
Name = input('What is your name?')
Age = int(input('What is your age?'))
FF = input('What is your favirote food?')
NF = Name.upper()
AF = Age + 1
FFF = FF
print(NF)
print(AF)
print(f'You love {FFF}!!')



#Challenge 10: Mini Quiz (1 Question)
A = int(input('What is 10 + 10?'))
if A == 20 :
  print('corret')
else: 
  print('failed')


#Challenge 8: Shopping Total with Bonus

p = int(input('What si the total?'))
if p > 1000:
  print('VIP')
elif p > 500:
  print('you got a water bottle.')


print(f'total:{p} baht.')
