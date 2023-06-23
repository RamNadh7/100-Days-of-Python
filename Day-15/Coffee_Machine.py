from art import logo
import time
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
}
money=0

def report(resources,money):
    for item in resources:
        print(f"{item}:{resources[item]}")
    print(f"Money : ${money}")
    return False


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry, there is not enough {item}")
            time.sleep(4)
            return False
    return True

def transaction(cost_of_drink):
    print("Please insert coins.")
    total=0
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    if total>=cost_of_drink:
        change=round(total-cost_of_drink,2)
        print(f"Take the change $ {change}")
        global money
        money+=cost_of_drink
        return True
    else:
        print("sorry, that's not enough money. Your Money is Refunded")
        return False

def prepare_item(item, ingredients):
    for ing in ingredients:
        resources[ing]-=ingredients[ing]
    print(f"Here is your {item} ☕. Enjoy")
    time.sleep(4)



Is_Machine_On=True


while Is_Machine_On:
    print(logo)
    usr_choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if usr_choice=="off":
        Is_Machine_On=False
    elif usr_choice=="report":
        Is_Machine_On=report(resources,money)
    else:
        if usr_choice in MENU:
            item=MENU[usr_choice]
            if is_resource_sufficient(item["ingredients"]):
                if transaction(item['cost']):
                    prepare_item(usr_choice,item['ingredients'])
        else:
            print("Invalid item choosen. Please select again from Menu")
