class Bank:
    __balance = 10000

    def get_balance(self):
        print("Total Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Amount Deposited:", amount)
        print("Updated Balance:", self.__balance)

    def withdrawal(self, amount):
        if self.__balance < amount:
            print("Insufficient Fund")
        else:
            self.__balance -= amount
            print("Withdrawal Amount :", amount)
            print("Updated Balance:", self.__balance)


bank1 = Bank()

bank1.get_balance()
bank1.deposit(10000)
bank1.withdrawal(12000)
bank1.__balance = 100000000000000000000000000
bank1.withdrawal(100000)
bank1.get_balance()