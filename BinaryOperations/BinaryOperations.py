# function which converts a string to a mathematical expresion
def operation_conversion(x, y, op):
    conversion = eval(op)
    return conversion


# I created a class named BinaryOperations in which I implemented several functions for the properties related to binary operations
class BinaryOperations:

    # functions which reads the binary operations and the set from the console
    def read_function(self):
        self.operation = input("Enter the binary operation: ")
        self.set = []
        self.no_elements = int(input("Enter the number of elements in the set A: "))

        for i in range(0, self.no_elements):
            x = int(input())
            self.set.append(x)

    # function which prints the binary operation
    def operation_print(self):
        print("The binary operation is " + self.operation)

    # function which checks the comutative property
    def operation_commutative(self):
        ok = True
        for i in self.set:
            for j in self.set:
                if operation_conversion(i, j, self.operation) != operation_conversion(j, i, self.operation):
                    ok = False
                    break

        if ok == True:
            return 1

        else:
            return 0

    # function which checks the associative property
    def operation_associative(self):
        ok = True
        for i in self.set:
            for j in self.set:
                for k in self.set:
                    d = operation_conversion(i, j, self.operation)
                    e = operation_conversion(j, k, self.operation)
                    if operation_conversion(i, e, self.operation) != operation_conversion(d, k, self.operation):
                        ok = False
                        break

        if ok == True:
            return 1
        else:
            return 0

    # function which checks the existance of a neutral element and if each element of the set is symmetrizable
    def operation_neutral_element_and_reverse(self):
        length_set = len(self.set)
        i = 0
        check_en = 0
        while length_set != 0:
            neutral_element = self.set[i]
            for j in self.set:
                if operation_conversion(neutral_element, j, self.operation) != j or operation_conversion(j,
                                                                                                         neutral_element,
                                                                                                         self.operation) != j:
                    i = i + 1
                    break
                elif operation_conversion(neutral_element, j, self.operation) == j and operation_conversion(j,
                                                                                                            neutral_element,
                                                                                                            self.operation) == j:
                    check_en = 1

            length_set = length_set - 1

        if check_en == 1:
            check_es = 1
            for i in self.set:
                for reverse in self.set:
                    if operation_conversion(i, reverse, self.operation) != neutral_element or operation_conversion(
                            reverse, i, self.operation) != neutral_element:
                        check_es = 0
                        break

            if check_es == 1:
                return 1
            else:
                return 0

        else:
            return 0

    # function which checks the group / commutative group property
    def operation_group(self):
        if self.operation_neutral_element_and_reverse() == 1 and self.operation_associative() == 1:
            print("The binary operation is a group")

        elif self.operation_neutral_element_and_reverse() == 1 and self.operation_associative() == 1 and self.operation_commutative() == 1:
            print("The binary operation is a commutative group")

        else:
            print("The binary operation is not a group")