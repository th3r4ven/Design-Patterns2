from printer import Printer


class Subtraction(object):

    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def rate(self):
        return self.__left_expression.rate() - self.__right_expression.rate()

    def accept(self, visitor):
        visitor.subtraction_visitor(self)

    @property
    def left_expression(self):
        return self.__left_expression

    @property
    def right_expression(self):
        return self.__right_expression


class Addition(object):

    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def rate(self):
        return self.__left_expression.rate() + self.__right_expression.rate()

    def accept(self, visitor):
        visitor.addition_visitor(self)

    @property
    def left_expression(self):
        return self.__left_expression

    @property
    def right_expression(self):
        return self.__right_expression


class Number(object):
    def __init__(self, number):
        self.__number = number

    def rate(self):
        return self.__number

    def accept(self, visitor):
        visitor.number_visitor(self)


if __name__ == '__main__':

    left_expression = Addition(Number(10), Number(20))
    right_expression = Addition(Number(5), Number(2))
    total = Addition(left_expression, right_expression)

    printer = Printer()

    total.accept(printer)
    print('\n\n#########\n')

    left_expression = Subtraction(Number(100), Number(200))
    right_expression = Addition(Number(5), Number(5))

    total = Addition(left_expression, right_expression)

    total.accept(printer)

