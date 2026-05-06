#this portion of the code is to generate a random number between -1000 and 1000, this is the telix encryption method, where the number generated will be used to shift the ASCII values of the characters in the entered word, phrase or sentence to create the encrypted message.
import random
import operator

num = random.randint(-1000,1000)
op_symbol = random.choice(["+", "-","*","/"])
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/":operator.truediv}
op_func = ops[op_symbol]
print(num, "is the number generated ", "and the operation is ", op_symbol)

num_entered = input("Enter a random number: ")
num_entered = int(num_entered)

print("type 1")
type_1_result = op_func(num_entered, num)
print("(numberEntered _ Operation _ randomnumber) This is output 1 : " , type_1_result)

print("type 2")
type_2_result = op_func(num, num_entered)
print("(randomnumber _ Operation _ numberEntered) This is output 2" , type_2_result)

response = input("Do you want to reverse? : ")
response = str(response)

if response in ['y', 'Y', "Yes", "yes"]:
    # this is the reversal section
    if op_symbol == '+':
        print("\n--- Reversing for addition ---")
        print("Reversing type 1")
        recovered_random = type_1_result - num_entered
        recovered_entered = type_1_result - num
        print(f"From type 1 result ({type_1_result}):")
        print(f"  - Recovered random number: {recovered_random} (original was {num})")
        print(f"  - Recovered entered number: {recovered_entered} (original was {num_entered})")
    
        print("\nReversing type 2")
        recovered_entered_v2 = type_2_result - num
        recovered_random_v2 = type_2_result - num_entered
        print(f"From type 2 result ({type_2_result}):")
        print(f"  - Recovered entered number: {recovered_entered_v2} (original was {num_entered})")
        print(f"  - Recovered random number: {recovered_random_v2} (original was {num})")

    elif op_symbol == '-':
        print("\n--- Reversing for subtraction ---")
        print("Reversing type 1")
        # type_1_result = num_entered - num
        recovered_entered = type_1_result + num
        recovered_random = num_entered - type_1_result
        print(f"From type 1 result ({type_1_result}):")
        print(f"  - Recovered entered number: {recovered_entered} (original was {num_entered})")
        print(f"  - Recovered random number: {recovered_random} (original was {num})")
    
        print("\nReversing type 2")
        # type_2_result = num - num_entered
        recovered_random_v2 = type_2_result + num_entered
        recovered_entered_v2 = num - type_2_result
        print(f"From type 2 result ({type_2_result}):")
        print(f"  - Recovered random number: {recovered_random_v2} (original was {num})")
        print(f"  - Recovered entered number: {recovered_entered_v2} (original was {num_entered})")
    
    elif op_symbol == '*':
        print("\n--- Reversing for multiplication ---")
        print("Reversing type 1")
        if num_entered != 0:
            # type_1_result = num_entered * num
            recovered_random = type_1_result / num_entered
            recovered_entered = type_1_result / num
            print(f"From type 1 result ({type_1_result}):")
            print(f"  - Recovered random number: {recovered_random} (original was {num})")
            print(f"  - Recovered entered number: {recovered_entered} (original was {num_entered})")
        else:
            print("Cannot reverse type 1: numberEntered is zero")
    
        print("\nReversing type 2")
        if num != 0:
            # type_2_result = num * num_entered
            recovered_entered_v2 = type_2_result / num
            recovered_random_v2 = type_2_result / num_entered
            print(f"From type 2 result ({type_2_result}):")
            print(f"  - Recovered entered number: {recovered_entered_v2} (original was {num_entered})")
            print(f"  - Recovered random number: {recovered_random_v2} (original was {num})")
        else:
            print("Cannot reverse type 2: randomnumber is zero")

    elif op_symbol == '/':
        print("\n--- Reversing for division ---")
        print("Reversing type 1")
        if num != 0:
            # type_1_result = num_entered / num
            recovered_entered = type_1_result * num
            recovered_random = num_entered / type_1_result if type_1_result != 0 else "undefined"
            print(f"From type 1 result ({type_1_result}):")
            print(f"  - Recovered entered number: {recovered_entered} (original was {num_entered})")
            if type_1_result != 0:
                print(f"  - Recovered random number: {recovered_random} (original was {num})")
            else:
                print(f"  - Recovered random number: {recovered_random} (cannot divide by zero)")
        else:
            print("Cannot reverse type 1: randomnumber is zero")
    
        print("\nReversing type 2")
        if num_entered != 0:
            # type_2_result = num / num_entered
            recovered_random_v2 = type_2_result * num_entered
            recovered_entered_v2 = num / type_2_result if type_2_result != 0 else "undefined"
            print(f"From type 2 result ({type_2_result}):")
            print(f"  - Recovered random number: {recovered_random_v2} (original was {num})")
            if type_2_result != 0:
                print(f"  - Recovered entered number: {recovered_entered_v2} (original was {num_entered})")
            else:
                print(f"  - Recovered entered number: {recovered_entered_v2} (cannot divide by zero)")
        else:
            print("Cannot reverse type 2: numberEntered is zero")

else:
    print("Goodbye World! ")
