class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2 / self.num1


obj = Calculator(10, 94)
print("Addition of given numbers : ",obj.add())
print("Substraction of given numbers : ",obj.subtract())
print("Multiplication of given numbers : ",obj.multiply())
print("Division of given numbers : ",obj.divide())