class subtraction(object):

    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def rate(self):
        return self.__left_expression.rate() - self.__right_expression.rate()


class Addition(object):

    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def rate(self):
        return self.__left_expression.rate() + self.__right_expression.rate()


class Number(object):
    def __init__(self, number):
        self.__number = number

    def rate(self):
        return self.__number


if __name__ == '__main__':

    left_expression = Addition(Number(10), Number(20))
    right_expression = Addition(Number(5), Number(2))
    total = Addition(left_expression, right_expression)
    print(total.rate())
