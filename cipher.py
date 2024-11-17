# add your code here
message = "python is fun!"
shift = 5
result = ""

# go through each of the letters in the message
# letter to represent input from variable message.
for letter in message:
    if letter.isalpha():
    #convert character
        letter_code = ord(letter)
        new_letter_code = shift + letter_code
    #chr returns the character corresponding to that code point
        new_character = chr(new_letter_code)
    #each time loop through, going to append new_character. 
        result += new_character
    else:
        result += letter
print(result)