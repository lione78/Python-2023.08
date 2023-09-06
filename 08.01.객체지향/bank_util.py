import datetime as dt
from account import Account

def create_account(account_list):
    account_info = input('이름, 금액 입력> ').split()
    ano, balance = account_info[0], int(account_info[1])
    now = dt.datetime.now()
    acc = Account(f"{now.strftime('%H%M%S')}", ano, balance)
    account_list.append(acc)

def deposit(account_list):
    cmd = input('계좌번호 출금금액 입력 > ').split()
    ano, amount = cmd[0], int(cmd[1])
    for acc in account_list:
        if acc.ano == ano:
            acc.deposit(amount)

def withdraw(account_list):
    cmd = input('계좌번호 인출금액 입력 > ').split()
    ano, amount = cmd[0], int(cmd[1])
    for acc in account_list:
        if acc.ano == ano:
            acc.withdraw(amount)