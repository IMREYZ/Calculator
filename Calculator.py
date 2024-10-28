class Calculator:
    def __init__(self, first, second, operation):
        self.first = first
        self.second = second
        self.operation = operation

    def exception(self):
        if type(self.first) not in [int, float]:
            raise TypeError('Первое число некорректное!')

        if type(self.second) not in [int, float]:
            raise TypeError('Второе число некорректное!')

        if self.operation not in ['+', '-', '/', '*']:
            raise ValueError('Оператор некорректный!')

        if self.operation == '/' and self.second == 0:
            raise ZeroDivisionError('На 0 делить нельзя!')

    def getResultOperation(self):
        self.exception()

        if self.operation == '+': self.result = self.plus()
        if self.operation == '-': self.result = self.minus()
        if self.operation == '*': self.result = self.multiplication()
        if self.operation == '/': self.result = self.division()

        return self.result

    def plus(self):
        return round(self.first + self.second, 10)

    def minus(self):
        return round(self.first - self.second, 10)

    def multiplication(self):
        return round(self.first * self.second, 10)

    def division(self):
        return round(self.first / self.second, 10)





