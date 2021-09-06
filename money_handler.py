
from items import CoffeeMachineItemList

item_list = CoffeeMachineItemList()


class MoneyHandler:

    def __init__(self):
        self.money = 0
        self.inserted_money = 0

    def report(self):
        print(f"Money: {self.money}$")

    def payment_processing(self, user_input):
        while True:
            item_cost = item_list.items[user_input]['money']

            print(f"Your drink costs {item_cost}$\n"
                  f"Your funds are {round(self.inserted_money, 2)}$\n")
            try:
                money_input = float(input("Insert Money (Write number)\n"))
            except ValueError:
                print("INPUT ERROR\n"
                      "Only numbers allowed!\n")
                continue
            else:
                self.inserted_money += money_input
                break

        if self.inserted_money < item_cost:
            print("Insufficient funds!")
            self.payment_processing(user_input)
        elif self.inserted_money == item_cost:
            print("Transaction successful!")
            self.inserted_money = 0
            self.money += item_cost
        else:
            change = self.inserted_money - item_cost
            print(f"Transaction successful. Your change amounts to {round(change, 2)}$")
            self.inserted_money = 0
            self.money += item_cost

