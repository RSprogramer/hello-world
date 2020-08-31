class Bank:

    balance = 0;

    def deposite(self):
        deposited = input("Enter amount to deposite :$");
        print("Amount deposited : $" + str(deposited))
        balance = deposited;
        return print("Deposite of amount $" + str(deposited) + " done succesful");

    def withdraw(self):
        withdrawal = input("Enter amount to withdraw :")
        return print("$" + withdrawal + " withdrawn");


    def bal():
        print("Your acct balance is : " + balance)


ob = Bank();

#print(ob.balance)

ob.deposite()
#ob.withdraw()





