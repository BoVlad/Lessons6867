class BankAccount:
    def __init__(self, passport, balance, name):
        self.__passport = passport
        self.__balance = balance
        self.__name = name
    def printinfo(self):
        print(self.__balance, self.__name)
    def getName(self):
        return self.__name
    def setName(self, new_name):
        self.__name = new_name

user = BankAccount("MP32363", 10000, "Kostya")
user.name = "Denis"