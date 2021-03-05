class Category:

    def __init__(self, category):
        ledger = []  # List of transactions that has taken place in this category
        balance = 0
        with_tot = 0
        self.category = category
        self.ledger = ledger
        self.balance = balance
        self.with_tot = with_tot

    def __str__(self,):
        return "\n{}\n{}".format(self.category.center(30, '*'), '\n'.join(map(str, self.ledger)))
        '''
        when category is printed, displays:
        
        ***********Category***********
        Transaction1(from ledger)
        Transaction2(from ledger)
        ...
        ...
        
        '''

    def deposit(self, dep_amount, desc='<NONE>'):
        self.ledger.append(f'Amount: {dep_amount}, Description: {desc}')
        self.balance += dep_amount

    def withdraw(self, with_amount, desc=''):
        if Category.check_funds(self, with_amount):
            self.with_tot += with_amount
            self.balance -= with_amount
            self.ledger.append(f'Amount: -{with_amount}, Description: {desc}')
            return True
        else:
            print('Cannot withdraw that much')
            return False

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return amount <= Category.get_balance(self)  # Checks if an amount can be taken out of the category balance

    def transfer(self, tr_amount, tr_category):
        if Category.check_funds(self, tr_amount):
            self.balance -= tr_amount
            self.ledger.append(f'Amount: -{tr_amount}, Description: Transfer to {tr_category.category.replace("*","")}')
            tr_category.balance += tr_amount
            tr_category.ledger.append(f'Amount: {tr_amount}, Description: Transfer from {self.category}')

        else:
            print('Insufficient funds to transfer')


def create_spend_chart(category_list):  # Creates a graph of %money spent from each category
    total_budget = 0
    budget_list_ratio = []
    for i in category_list:
        total_budget += i.with_tot
    for i in category_list:
        try:
            budget_list_ratio.append(round((i.with_tot/total_budget)*10))  # Calculates the proportion spent in each
        except ZeroDivisionError:                                          # category to the nearest 10%
            budget_list_ratio.append(0)
    # print(total_budget)
    # print(budget_list_ratio)

    list_point = []
    for i in budget_list_ratio:
        list_point.append(list('o'*i))  # creates the amount of points each category will be represented by
    # print(list_point)

    print('\n')
    for i in range(len(category_list)):
        print('{:10}|{}\n'.format(category_list[i].category, "   ".join(list_point[i])))
    print('           ' + '-'*45)
    print('           1   2   3   4   5   6   7   8   9   1   percentage')
    print('           0   0   0   0   0   0   0   0   0   0   spent per')
    print('                                               0   category')


food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")
rent = Category("Rent")

food.deposit(1000, "initial deposit")
food.transfer(50, clothing)
auto.deposit(1000, "initial deposit")
rent.deposit(1200, "initial deposit")

food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

clothing.withdraw(25.55)
clothing.withdraw(100)
auto.withdraw(15)
rent.withdraw(50, "rent")
auto.transfer(50, rent)

print(food)
print(clothing)
print(auto)
print(rent)

print(create_spend_chart([food, clothing, auto, rent]))
