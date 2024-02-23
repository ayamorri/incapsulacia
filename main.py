from random import choice

class Random:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def __get_result(self):
        oper = [ "+", "-", "*", "/"]
        operands = choice(oper)
        if operands == "+":
            return self.__a + self.__b
        elif operands == "-":
            return self.__a - self.__b
        elif operands == "*":
            return self.__a * self.__b
        elif operands == "/":
            return self.__a / self.__b
    def result(self):
        return self.__get_result()
    def __str__(self):
        return self.__get_result()

randomaizer = Random(2,20)
print(randomaizer.result())
print(randomaizer.__str__())
