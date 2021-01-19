from datetime import date
from abc import ABCMeta, abstractmethod


class Contract_state(object):
    __metaClass__ = ABCMeta

    @abstractmethod
    def new(self, contract):
        pass

    @abstractmethod
    def ongoing(self, contract):
        pass

    @abstractmethod
    def arranged(self, contract):
        pass

    @abstractmethod
    def done(self, contract):
        pass

    def __str__(self):
        pass


class New(Contract_state):

    def new(self, contract):
        raise Exception('This contract is already new')

    def ongoing(self, contract):
        contract.kind = Ongoing()

    def arranged(self, contract):
        raise Exception('Skip steps is not allowed, must be set as "ongoing" first')

    def done(self, contract):
        raise Exception('Skip steps is not allowed, must be set as "ongoing and arranged" first')

    def __str__(self):
        return "New"


class Ongoing(Contract_state):

    def new(self, contract):
        raise Exception('Rollback steps in this case is not allowed')

    def ongoing(self, contract):
        raise Exception('This contract is already on ongoing')

    def arranged(self, contract):
        contract.kind = Arranged()

    def done(self, contract):
        raise Exception('Skip steps is not allowed, must be set as "arranged" first')

    def __str__(self):
        return "Ongoing"


class Arranged(Contract_state):

    def new(self, contract):
        raise Exception('Rollback steps in this case is not allowed')

    def ongoing(self, contract):
        contract.kind = Ongoing()

    def arranged(self, contract):
        raise Exception('This contract is already on arranged')

    def done(self, contract):
        contract.kind = Done()

    def __str__(self):
        return "Arranged"


class Done(Contract_state):

    def new(self, contract):
        raise Exception('Rollback steps in this case is not allowed')

    def ongoing(self, contract):
        raise Exception('Rollback steps in this case is not allowed')

    def arranged(self, contract):
        raise Exception('Rollback steps in this case is not allowed')

    def done(self, contract):
        raise Exception('This contract is done')

    def __str__(self):
        return "Done"


class Contract(object):

    def __init__(self, cdate, client, contract_type=New()):
        self.__cdate = cdate
        self.__client = client
        self.__kind = contract_type

    @property
    def cdate(self):
        return self.__cdate

    @cdate.setter
    def cdate(self, cdate):
        self.__cdate = cdate

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self.__client = client

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        self.__kind = kind

    def ADVnew(self):
        self.__kind.ongoing(contract)

    def ADVongoing(self):
        self.__kind.arranged(contract)

    def ADVarranged(self):
        self.__kind.done(contract)

    def save_state(self):
        return State(Contract(
            self.__cdate,
            self.__client,
            self.__kind
        ))

    def restore_contract(self, state):
        self.__client = state.contract.client
        self.__cdate = state.contract.cdate
        self.__kind = state.contract.kind


class State(object):
    def __init__(self, contract):
        self.__contract = contract

    @property
    def contract(self):
        return self.__contract


class History(object):
    def __init__(self):
        self.__saved_states = []

    def get_state(self, index):
        return self.__saved_states[index]

    def add_state(self, state):
        self.__saved_states.append(state)


if __name__ == '__main__':
    history = History()

    contract = Contract(date.today(), 'Raven', New())

    contract.ADVnew()

    history.add_state(contract.save_state())

    contract.ADVongoing()

    history.add_state(contract.save_state())

    contract.ADVarranged()

    history.add_state(contract.save_state())

    print(contract.kind)

    contract.restore_contract(history.get_state(1))

    print(contract.kind)
