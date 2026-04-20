# import statements go here
import random
import operator

print("Welcome to the Cryptography Test Program!")
#Cryptography Test Program

#this portion of the code is to generate a random number between -1000 and 1000, this is the telix encryption method, where the number generated will be used to shift the ASCII values of the characters in the entered word, phrase or sentence to create the encrypted message.
num = random.randint(-1000,1000)
op_symbol = random.choice(["+", "-","*"])
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
op_func = ops[op_symbol]
print(num, "is the number generated ", "and the operation is ", op_symbol)

#This portion of the code is for the user to enter a word, phrase or sentence to be encrypted.
phrasetoscramble = input("Enter the word, phrase or sentence to be enctypted: ")
print(phrasetoscramble, " is the word you entered.")

EnteredPhrase = phrasetoscramble.upper()
print(EnteredPhrase, "is the word you entered in capitals")


#Ascii Conversion section
Ascii_Array = []


for c in EnteredPhrase:
    print(f"{c}: {ord(c)}")
    Ascii_Array = [ord(c) for c in EnteredPhrase]
    
print("This is the text you entered converted to ASCII:", Ascii_Array)

Shifted_Array = []
Shifted_Array = Ascii_Array
print("This is the shifted array:", Shifted_Array)

for i in Shifted_Array:
    Shifted_Array = [op_func(i,num) for i in Shifted_Array]
    
print("This is the final shifted array:", Shifted_Array)    