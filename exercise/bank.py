# class bankaccount:
#     def __init__(self,account_number,date_of_opening,balance,customer_name):
#         self.accno=account_number
#         self.dop=date_of_opening
#         self.bal=balance
#         self.name=customer_name

    
#     def deposit(self,amount):
#         self.bal+=amount
#         print(amount,"is deposited to your accounr")
    
#     def withdraw(self,amount):
#         if amount<=self.bal:
#             print(amount,"amount has been withdraw from your account" )

#     def check_balnce(self):
#         print("current balance is:",self.bal)

#     def customer_details(self):
#         print("name:",self.name) 
#         print("account number:",self.accno)
#         print("date of opening:",self.dop)
#         print("balnce:",self.bal)  

# acc_no_1=bankaccount(34568909864,"09-04-2005",1000,"pavi")
# acc_no_2=bankaccount(1234567908,"08-12-2004",5000,"suba")

# acc_no_1.customer_details()
# acc_no_2.customer_details()

# acc_no_1.deposit(4000)
# acc_no_2.check_balnce()

# acc_no_1.withdraw(500)

#using hierarchical

class Bank:
    def __init__(self, name):
        self.name = name

    def display_bank_name(self):
        print(f"Welcome to {self.name} Bank!")
              
class SavingsAccount(Bank):
    def __init__(self, name, interest_rate):
        super().__init__(name)
        self.interest_rate = interest_rate

    def calculate_interest(self, balance):
        interest = balance * (self.interest_rate / 100)
        print(f"Interest on your savings balance is: ${interest:.2f}")

class CurrentAccount(Bank):
    def __init__(self, name, overdraft_limit):
        super().__init__(name)
        self.overdraft_limit = overdraft_limit

    def check_overdraft(self, amount):
        if amount > self.overdraft_limit:
            print("Overdraft limit exceeded!")
        else:
            print(f"Transaction approved. Remaining overdraft limit: ${self.overdraft_limit - amount:.2f}")

# Creating objects of SavingsAccount and CurrentAccount
savings = SavingsAccount("Global Bank", 4.5)
current = CurrentAccount("Global Bank", 1000)

# Accessing parent and child methods
savings.display_bank_name()  # From Parent Class
savings.calculate_interest(2000)  # From SavingsAccount Class

current.display_bank_name()  # From Parent Class
current.check_overdraft(800)  # From CurrentAccount Class
current.check_overdraft(1200)  # Overdraft limit exceeded
