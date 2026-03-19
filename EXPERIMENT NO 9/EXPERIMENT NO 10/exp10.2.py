

class Add:
    def addition(self, a, b):
        print("Addition =", a + b)

class Sub:
    def subtraction(self, a, b):
        print("Subtraction =", a - b)


class Mul:
    def multiplication(self, a, b):
        print("Multiplication =", a * b)


class Div:
    def division(self, a, b):
        if b != 0:
            print("Division =", a / b)
        else:
            print("Division by zero not allowed")


class Calculator(Add, Sub, Mul, Div):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

obj = Calculator(20, 10)

print("Data1 =", obj.data1)
print("Data2 =", obj.data2)

obj.addition(obj.data1, obj.data2)
obj.subtraction(obj.data1, obj.data2)
obj.multiplication(obj.data1, obj.data2)
obj.division(obj.data1, obj.data2)                                                                                                                                                                                                                                                                          