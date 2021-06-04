MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

on = True


def make_report():
    for key, value in resources.items():
        print(key, ":", value)


def check_resources(drink):
    if drink in MENU:
        water_for_drink = MENU.get(drink).get("ingredients").get("water", 0)
        milk_for_drink = MENU.get(drink).get("ingredients").get("milk", 0)
        coffee_for_drink = MENU.get(drink).get("ingredients").get("coffee", 0)

        if resources["water"] < water_for_drink:
            print('Мало воды')
            return False
        elif resources["milk"] < milk_for_drink:
            print('Мало молока')
            return False
        elif resources["coffee"] < coffee_for_drink:
            print('Мало кофе')
            return False
        else:
            return True
    else:
        print('Нет такого напитка')
        return False


def process_coins():
    quarters = input('Сколько вы внесли монет по $0.25? ')
    dimes = input('Сколько вы внесли монет по $0.10? ')
    nickles = input('Сколько вы внесли монет по $0.05? ')
    pennies = input('Сколько вы внесли монет по $0.01? ')
    money_inserted = (0.25 * int(quarters)) + (0.10 * int(dimes)) + (0.05 * int(nickles)) + (0.01 * int(pennies))
    return round(money_inserted, 2)


def check_transaction(coins: float, drink: str):
    drink_cost = MENU.get(drink).get("cost")
    if drink_cost == coins:
        return True
    elif drink_cost < coins:
        change = coins - drink_cost
        print(f'Ваша сдача: ${round(change, 2)}')
        return True
    else:
        print('Вы внесли недостаточно денег. Возврат')
        return False


def make_drink(drink):
    water_for_drink = MENU.get(drink).get("ingredients").get("water", 0)
    milk_for_drink = MENU.get(drink).get("ingredients").get("milk", 0)
    coffee_for_drink = MENU.get(drink).get("ingredients").get("coffee", 0)
    drink_cost = MENU.get(drink).get("cost")
    resources["water"] -= water_for_drink
    resources["milk"] -= milk_for_drink
    resources["coffee"] -= coffee_for_drink
    resources["money"] += drink_cost


while on:
    user_answer = input("Какой напиток препочитаете? (espresso/latte/cappuccino): ")
    if user_answer == 'off':
        on = False
    elif user_answer == 'report':
        make_report()
    else:
        if check_resources(user_answer):
            print('Внесите деньги...')
            coins_in = process_coins()
            print(f"Вы внесли: ${coins_in}")
            if check_transaction(coins_in, user_answer):
                make_drink(user_answer)
                print(f"Ваш {user_answer}. Наслаждайтесь!")
