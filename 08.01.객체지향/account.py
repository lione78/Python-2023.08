class Account:
    def __init__(self, ano, name, balance):
        self.ano = ano
        self.name = name
        self.__balance = 0
        if 0 <= self.__balance <= 10000000:
            self.__balance = balance

    def deposit(self, amount):
        if self.__balance + amount > 10000000:
            print('금액이 초과되었습니다.')
            return
        self.__balance += amount
    
    def withdraw(self,amount):
        if self.__balance < amount:
            print('잔액이 부족합니다.')
            return
        self.__balance -= amount

    def __str__(self):
        return f'계좌번호 : {self.ano}, 소유주: {self.name}, 잔액: {self.__balance:<10,d}'