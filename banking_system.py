
class Account:
    def __init__(self,account_number:int, account_holder:str, account_balance:float = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__account_balance = account_balance

    def get_account_balance(self):
        return self.__account_balance
    
    def set_account_balance(self, new_balance):
        self.__account_balance += new_balance

user = Account(2046411464, "sultaanat", 12000)
print(user.get_account_balance())
print(user.set_account_balance(10000))

      


#     def deposit(self, deposit_amount:int):
#         if deposit_amount > 0:
#             self.account_balance += deposit_amount
#             print(f"You've successfully deposited {deposit_amount}. New account balance: {self.account_balance}")
#         else:
#             print(f"Invalid Deposit Amount")


#     def withdraw(self, withdraw_amount:int):
#         if withdraw_amount > 0 and withdraw_amount <= self.account_balance: 
#             self.account_balance -= withdraw_amount
#             self.account_balance = round(self.account_balance, 2)
#             print(f"You've successfully withdrew {withdraw_amount}. New account balance: {self.account_balance}")
#         else:
#             print(f"Invalid or Insufficient Withdrawal Amount")

#     def transfer(self, transfer_amount:int, targeted_account):
#         if transfer_amount > 0 and transfer_amount <= self.account_balance:
#             self.account_balance -= transfer_amount
#             self.account_balance = round(self.account_balance, 2)
#             targeted_account.deposit(transfer_amount)
#             print(f"You've successfully transfered {transfer_amount} to {targeted_account}. Your new balance is {self.account_balance}.")

#     def __str__(self):
#         return f"Account number: {self.account_number}, Account holder: {self.account_holder}, balance: {self.account_balance}"
    

# user = Account(2046411464, "sultaanat", 12000.3)
# user.deposit(100000)

# user = Account(2046411464, "sultaanat", 12000.3)
# user.withdraw(10000)

# # user = Account(2046411464, "sultaanat", 12000.3)
# # user.transfer(10000, 1234567891)


# class Bank:
#     def __init__(self,):
#         self.accounts = []

#     def createAccount(self, account_number, account_holder, account_balance=0.0):

#         def find_account(self, account_number):
#             for account in self.accounts:
#                 if account.account_number == account_number:
#                     return account
#                 return None
    
#         if self.find_account(account_number):
#             print(f"Account number {account_number} already exists")
#         else:
#             def gen_account_details(full_name):
#                 account_number = random(10)
#                 print(account_number)

#             gen_account_details(Bashir)
#             # new_account = Account(account_number, account_holder, account_balance)
#             # self.accounts.append(new_account)
#             # print("Account Created successfully")


# def gen_account_details(full_name):
#                 account_number = random.randint(1000000000, 9999999999)
#                 print(f"Your Account no is: {account_number}")

# gen_account_details("Bashir") 