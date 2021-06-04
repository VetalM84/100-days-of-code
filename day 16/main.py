from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_all = Menu()
coffee_machine = CoffeeMaker()
money_register = MoneyMachine()

on = True

while on:
    items = menu_all.get_items()
    user_answer = input(f"Какой напиток препочитаете? {items}: ")
    if user_answer == 'off':
        on = False
    elif user_answer == 'report':
        coffee_machine.report()
        money_register.report()
    else:
        search_drink = menu_all.find_drink(user_answer)
        if coffee_machine.is_resource_sufficient(search_drink):
            check_transaction = money_register.make_payment(search_drink.cost)
            # print(f"Вы внесли: ${check_transaction}")
            if check_transaction:
                coffee_machine.make_coffee(search_drink)
