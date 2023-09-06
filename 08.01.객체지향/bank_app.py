import sys, os
from account import Account
import bank_util as bu
import joblib as jl

file_name = 'account.jl'
if os.path.exists(file_name):
    account_list = jl.load(file_name)
else:
    account_list = []

while True:
    menu_no = int(input('1:계좌생성, 2:계좌목록, 3:입금, 4:출금, 5:종료> '))
    if menu_no == 1:
        bu.create_account(account_list)
    elif menu_no == 2:
        for acc in account_list:
            print(acc)
    elif menu_no == 3:
        bu.deposit(account_list)
    elif menu_no == 4:
        bu.withdraw(account_list)
    elif menu_no == 5:
        jl.dump(account_list, 'account.jl')
        sys.exit()
    else:
        print('올바른 숫자를 입력하세요.')
