alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
key = input('Please enter the key: ')
key = int(key)
new_message = ''

message = input('Please enter a message: ')
for character in message:
    if character in alphabet:
    	position = alphabet.find(character)

    	new_position = (position + key) % 26

    	new_character = alphabet[new_position]

    	new_message += new_character
    elif character in alphabet_upper:
      position = alphabet_upper.find(character)
      
      new_position = (position + key) % 26
      
      new_character = alphabet_upper[new_position]
      
      new_message += new_character
    elif character in numbers:
      position = numbers.find(character)
      new_position = (position + key) % 10
      new_character = numbers[new_position]
      new_message += new_character
    else:
        new_message += character
print(new_message)







