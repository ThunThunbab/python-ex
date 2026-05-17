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
P = input('What is the passcode?')

if U == 'admin' and  P == '1234':
  print('LOGIN SUCCESS')
 
else:
  print("Login Failed")



#Challenge 5: Mini Profile Generator
Name = input('What is your name?')
Age = int(input('What is your age?'))
FF = input('What is your favirote food?')
NF = Name.upper()
AF = Age + 1
print(NF)
print(AF)
print(f'You love {FF}!!')



#Challenge 10: Mini Quiz (1 Question)
A = int(input('What is 10 + 10?'))
if A == 20 :
  print('corret')
else: 
  print('failed')


#Challenge 8: Shopping Total with Bonus

p = float(input('What si the total?'))
if p > 1000:
  print('VIP')
elif p > 500:
  print('you got a water bottle.')


print(f'total:{p} baht.')

#Challenge 6: Even or Odd Checker

input = int(input('Enter number.'))
if input%2 == 0:
  print('EVEN')
else:
  
  

  print('ODD')
  
  
#Challenge 7: Simple Grade Checker

score = int(input('Enter your score.'))
if score >= 80:
  print('Excellent')
elif score >= 50 :
  print('Pass')
else:
  print('Fail')
  
#Challenge 9: Password Strength Checker
paco = input('What is your passcode?')
if len(paco) < 6:
  print('This is a week pass code!!.')
else:
  print("good passcode")
  
#Challenge 3: Temperature Checker

Celsius = int(input('Enter temp C'))
kevken = Celsius+273
print(f'Kelvin is {kevken}')
if Celsius > 30:
  print('Hot!! Hot!!!')
elif Celsius < 20:
  print('Thhiiissss iissss soooo cooolld!!')
else:
  print('perfect weather today')
