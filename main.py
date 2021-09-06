
from money_handler import MoneyHandler
from coffee_maker import CoffeeMaker

coffee_maker = CoffeeMaker()
money_handler = MoneyHandler()

while True:
    user_input = input("\nHello! Would you like some coffee?\n"
                       "Press:\n"
                       "1 for Cappuccino\n"
                       "2 for Latte Macchiato\n"
                       "3 for Espresso\n\n"
                       "Your choice: ")

    if user_input == "off":
        break
    elif user_input == "report":
        coffee_maker.report()
        money_handler.report()
    elif user_input == "refill":
        coffee_maker.refill()
    elif user_input == "1" or user_input == "2" or user_input == "3":
        if coffee_maker.check_resources_sufficient(user_input):
            money_handler.payment_processing(user_input)
            coffee_maker.make_coffee(user_input)

        else:
            print("Sorry, not enough resources. Call XXX")
    else:
        print("INPUT ERROR\n"
              "Try again.")
