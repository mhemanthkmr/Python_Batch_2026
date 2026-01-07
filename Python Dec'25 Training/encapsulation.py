class Bank:
    __balance = 1000
    username = "Raj"
    account_number = 123459876

    def deposit(self):
        try:
            deposit_amount = float(input("Enter a amount to Deposit :"))
            self.__balance += deposit_amount
            self._get_balance()
        except Exception as err:
            print("Invalid Amount")

    def withdraw(self):
        try:
            withdraw_amount = float(input("Enter a amount to Withdraw :"))
            if withdraw_amount <= self.__balance:
                self.__balance -= withdraw_amount
                self._get_balance()
            else:
                print("Insufficient Fund")
        except:
            print("Invalid Amount")

    def _get_balance(self):
        print("Your Bank Balance is:", self.__balance)


obj1 = Bank()
obj1.deposit()
obj1.withdraw()
obj1._get_balance() 
