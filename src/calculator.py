class Calculator:
    def CheckParameter(*args):
        for value in args:
            if(not isinstance(value,(int,float))):
                raise TypeError('thats not a number.')
    
    @staticmethod
    def sum(num1, num2):
        Calculator.CheckParameter(num1,num2)
        return round(num1 + num2,2)

    @staticmethod
    def divide(num1, num2):
        Calculator.CheckParameter(num1,num2)
        return round(num1 / num2,2)

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2