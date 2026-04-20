#Cryptography Test Program

print("Enter sentence or word to be phrased")
phrasetoscramble = input("Enter the word, phrase or sentence to be enctypted: ")
print(phrasetoscramble, " is the word you entered.")

EnteredPhrase = phrasetoscramble.upper()
print(EnteredPhrase, "is the word you entered in capitals")

Ascii_Array = []

for c in EnteredPhrase:
    print(f"{c}: {ord(c)}")
    Ascii_Array = [ord(c) for c in EnteredPhrase]
    
print(Ascii_Array)

Shifted_Array = []
for i in Ascii_Array:
    i+
    print()
