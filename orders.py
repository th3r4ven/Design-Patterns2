from datetime import date
from abc import ABCMeta, abstractmethod


class Orders(object):
    def __init__(self, client, value):
        self.__client = client
        self.__value = value
        self.__status = 'NEW'
        self.__final_date = None

    def pay(self):
        self.__payed = 'PAYED'

    def end_order(self):
        self.__final_date = date.today()
        self.__status = 'DELIVERED'

    @property
    def client(self):
        return self.__client

    @property
    def value(self):
        return self.__value

    @property
    def status(self):
        return self.__status

    @property
    def terminate_date(self):
        return self.__final_date


class Command(object):

    __metaClass__ = ABCMeta

    @abstractmethod
    def run(self):
        pass


class End_order(Command):

    def __init__(self, order):
        self.__order = order

    def run(self):
        self.__order.end_order()


class Pay_order(Command):

    def __init__(self, order):
        self.__order = order

    def run(self):
        self.__order.pay()


class Workflow(object):

    def __init__(self):
        self.__commands = []

    def add_command(self, command):
        self.__commands.append(command)

    def proccess(self):
        for command in self.__commands:
            command.run()


if __name__ == '__main__':
    order1 = Orders('Raven', 200)
    order2 = Orders('Th3Raven', 1000)
    workflow = Workflow()

    workflow.add_command(End_order(order1))
    workflow.add_command(Pay_order(order1))
    workflow.add_command(End_order(order2))

    workflow.proccess()
