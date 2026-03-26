class Factorial:
    def __init__(self):
        pass

    def factorial_recursion(self,num):
        if num <= 1:
            return 1
        return num * (self.factorial_recursion(num - 1))

    def factorial_iterative(self,num):
        fact = 1
        for i in range(num,0,-1):
            fact = fact * i
        return fact

factorial = Factorial()
print(factorial.factorial_iterative(5))