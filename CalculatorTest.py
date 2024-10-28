from unittest import *
from Calculator import Calculator

class CalculatorTest(TestCase):
    # Обычные ариф. операции (без исключений)

    # + (int)
    def testPlus1(self):
        calcPlus1 = Calculator(3, 5, '+')
        resultPlus1 = calcPlus1.getResultOperation()

        self.assertEqual(resultPlus1, 8)


    # + (float)
    def testPlus2(self):
        calcPlus2 = Calculator(2.4, 5, '+')
        resultPlus2 = calcPlus2.getResultOperation()

        self.assertEqual(resultPlus2, 7.4)


    # - (int)
    def testMinus1(self):
        calcMinus1 = Calculator(10, 7, '-')
        resultMinus1 = calcMinus1.getResultOperation()

        self.assertEqual(resultMinus1, 3)


    # - (float)
    def testMinus2(self):
        calcMinus2 = Calculator(6.3, 7, '-')
        resultMinus2 = calcMinus2.getResultOperation()

        self.assertEqual(resultMinus2, -0.7)


    # * (int)
    def testMultiplication1(self):
        calcMultiplication1 = Calculator(6, 8, '*')
        resultMultiplication1 = calcMultiplication1.getResultOperation()

        self.assertEqual(resultMultiplication1, 48)


    # * (float)
    def testMultiplication2(self):
        calcMultiplication2 = Calculator(5.2, 6, '*')
        resultMultiplication2 = calcMultiplication2.getResultOperation()

        self.assertEqual(resultMultiplication2, 31.2)


    # / (int)
    def testDivision1(self):
        calcDivision1 = Calculator(-30, 5, '/')
        resultDivision1 = calcDivision1.getResultOperation()

        self.assertEqual(resultDivision1, -6)


    # / (float)
    def testDivision2(self):
        calcDivision2 = Calculator(8, 5, '/')
        resultDivision2 = calcDivision2.getResultOperation()

        self.assertEqual(resultDivision2, 1.6)




    # Исключения

    # Деление на 0
    def testException1(self):
        calcException1 = Calculator(2, 0, '/')

        with self.assertRaisesRegex(ZeroDivisionError, 'На 0 делить нельзя!'):
            calcException1.getResultOperation()


    # Первое число некорректное!
    def testException2(self):
        calcException2 = Calculator('a', 3, '/')

        with self.assertRaisesRegex(TypeError, 'Первое число некорректное!'):
            calcException2.getResultOperation()


    # Второе число некорректное!
    def testException2(self):
        calcException2 = Calculator(3, 'q', '*')

        with self.assertRaisesRegex(TypeError, 'Второе число некорректное!'):
            calcException2.getResultOperation()


    # Оператор некорректный!
    def testException2(self):
        calcException2 = Calculator(5, 3, ':')

        with self.assertRaisesRegex(ValueError, 'Оператор некорректный!'):
            calcException2.getResultOperation()



