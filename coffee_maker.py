
from items import CoffeeMachineItemList

items_list = CoffeeMachineItemList()


class CoffeeMaker:

    def __init__(self):
        self.water = 1000
        self.milk = 1000
        self.coffee = 1000

    def make_coffee(self, user_input):

        water_cost = items_list.items[user_input]["water"]
        milk_cost = items_list.items[user_input]["milk"]
        coffee_cost = items_list.items[user_input]["coffee"]

        self.water -= water_cost
        self.milk -= milk_cost
        self.coffee -= coffee_cost

        print("Your coffee is ready. Enjoy!")

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}ml")

    def check_resources_sufficient(self, user_input):
        if self.water >= items_list.items[user_input]["water"] and self.milk >= items_list.items[user_input]["milk"] \
                and self.coffee >= items_list.items[user_input]["coffee"]:
            return True
        else:
            return False

    def refill(self):
        self.water = 1000
        self.milk = 1000
        self.coffee = 1000
        print("Refilled!")
