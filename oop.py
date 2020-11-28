class AccountHolder(object):
    total = 0
    def __init__(self, acc_no, name, age, bal):
            self.acc_no = acc_no
            self.name = name
            self.age = age
            self.bal = bal
            AccountHolder.total = AccountHolder.total + 1

    def __repr__(self):
            return "\nName: {}\nBalance: {:10.2f}\n".format(self.name, self.bal) 

    def update(self, new_bal):
            print("Old balance:", self.bal)
            self.bal = new_bal
            print("New balance:", self.bal)

    def totalAccHolders():
            print("Total no of account holders:", AccountHolder.total)
    totalAccHolders = staticmethod(totalAccHolders)
class SavingAccHolder(AccountHolder):
    def __init__(self,acc_no,name,age,bal):
            super().__init__(acc_no,name,age,bal)

    def deposit_bal(self,y):
    
            super().update(self.bal+y)
    
    
class LoanAccHolder(AccountHolder):
    def __init__(self,acc_no,name,age,bal):
            super().__init__(acc_no,name,age,bal)

    def withdraw_bal(self,x):
    
            super().update(self.bal-x)


print("MENU")
print("1. Create a new AccountHolder")
print("2. Update AccountHolder balance")
print("3.Withdraw Money")
print("4.Deposit Money")
print("5.No. of holders")
listAcc = []
AccountHolder.totalAccHolders()
while(True):
    op = int(input("Enter option"))
    if op==1:
            listAcc.append(AccountHolder(int(input("Enter AccNo:")),input("Enter Name:"),int(input("Enter age")),float(input("Enter balance"))))
            print(listAcc[-1])
            AccountHolder.totalAccHolders()
    elif op==2:
            s = input("Enter name")
            for a in listAcc:
                    if s == a.name:
                            bal = float(input("Enter new balance"))
                            a.update(bal)
    elif op==4:
            sav=SavingAccHolder(int(input("Enter AccNo:")),input("Enter Name:"),int(input("Enter age")),float(input("Enter balance")))
            x=int(input("enter amount to deposit"))
            sav.deposit_bal(x)
    elif op==3:
            loan=LoanAccHolder(int(input("Enter AccNo:")),input("Enter Name:"),int(input("Enter age")),float(input("Enter balance")))
            y=int(input("Enter amount to withdraw"))
            loan.withdraw_bal(y)
    elif op==5:
            AccountHolder.totalAccHolders()
            
    else:
            print("Invalid input")
            break
                                  
