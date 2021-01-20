class Printer(object):

    def addition_visitor(self, add):

        print('(', end="")
        add.left_expression.accept(self)
        print('+', end="")
        add.right_expression.accept(self)
        print(')', end="")

    def subtraction_visitor(self, subtraction):
        print('(', end="")
        subtraction.left_expression.accept(self)
        print('-', end="")
        subtraction.right_expression.accept(self)
        print(')', end="")

    def number_visitor(self, number):
        print(number.rate())
