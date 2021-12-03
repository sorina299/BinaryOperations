from BinaryOperations import *

b_op = BinaryOperations()  # I created a binary operation object
b_op.read_function()  # I called the read_function from the class using the variable in which I saved the binary operation object

# This menu helps the user to choose what he wants to do with the binary operation
print("\nMENU")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
print("*  1. Print the binary operation                                        *")
print("*  2. Check if the binary operation is commutative                      *")
print("*  3. Check if the binary operation is associative                      *")
print("*  4. Check if the binary operation is a group or a commutative group   *")
print("*  5. Exit                                                              *")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

while True:
    case = int(input("\nEnter your option: "))

    if case == 1:
        b_op.operation_print()
    elif case == 2:
        if b_op.operation_commutative() == 1:
            print("The binary operation is commutative")
        else:
            print("The binary operation is not commutative")
    elif case == 3:
        if b_op.operation_associative() == 1:
            print("The binary operation is associative")
        else:
            print("The binary operation is not associative")
    elif case == 4:
        b_op.operation_group()

    elif case == 5:
        break
