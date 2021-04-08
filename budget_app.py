class BudgetApp :

    def __init__(self, category):
        self.amounts = []
        self.category = category

    # depositOperation
    def depositOperation(self,amount):
        self.amounts.append(amount)

    # withdrawalOperation
    def withdrawalOperation(self,amount):
        if self.check_funds(amount):
            self.amounts.append(-amount)
            return True
        else:
            return False

    # balanceOperation
    def balanceOperation(self):
        balance = 0
        for i in self.amounts:
            balance += i
        return balance

    # transfertOperation
    def transferOperation(self, amount, name):
        if self.check_funds(amount):
            self.withdrawalOperation(amount)
            name.depositOperation(amount)
            return True
        else:
            return False

    #checks if the account has the necessary amount
    def check_funds(self, amount):
        if amount <= self.balanceOperation():
            return True
        else:
            return False



# food category
food = BudgetApp("Food")

# cloting category
clothing = BudgetApp("Clothing")

# entertainment category
entertainment = BudgetApp("Entertainment")

# different operations
food.depositOperation(1000)
food.withdrawalOperation(150)
food.transferOperation(200,clothing)

clothing.depositOperation(100)
clothing.withdrawalOperation(50)
clothing.transferOperation(50,entertainment)

entertainment.depositOperation(500)


print(f"The Current balance in {food.category} is {food.balanceOperation()}")
print(f"The Current balance in {clothing.category} is {clothing.balanceOperation()}")
print(f"The Current balance in {entertainment.category} is {entertainment.balanceOperation()}")
