MENU = {
    "gullan": {
        "ingredienser": {
            "whiskey": 4,
            "bailey": 6,
            "coffee": 20
        },
        "pris": 39,
    },
    "mumman": {
        "ingredienser": {
            "vodka": 4,
            "whiskey": 2,
            "thai-tea": 18,
            "bananlikör": 6,
        },
        "pris": 44,
    },
    "frugan": {
        "ingredienser": {
            "vodka": 4,
            "whiskey": 4,
            "bailey": 4,
            "coffee": 10,
            "sodawater": 8,
        },
        "pris": 52,
    },
    "beauty": {
        "ingredienser": {
            "vodka": 10,
            "sodawater": 10,
            "thai-tea": 10,
        },
        "pris": 40,
    },
    "fizz": {
        "ingredienser": {
            "vodka": 4,
            "bailey": 6,
            "thai-tea": 12,
            "bananlikör": 8,
        },
        "pris": 43,
    },
    "buzz": {
        "ingredienser": {
            "thai-tea": 10,
            "coffee": 5,
            "sodawater": 15,
        },
        "pris": 19,
    },
}

def is_resource_sufficient(order_ingredients):
    '''Returns True when orders can be made, False if ingredients are insufficient.'''
    for item in order_ingredients:
        if order_ingredients[item] > stock[item]:
            print(f"sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    '''Returns the total calculated from the coins inserted.'''
    print("Please insert coins")
    total = int(input("Hur många 10Kr?: ")) * 10
    total += int(input("Hur många 5Kr?: ")) * 5
    total += int(input("Hur många 2Kr?: ")) * 2
    total += int(input("Hur många 1Kr?: "))
    return total

def is_transaction_successful(payment, drink_cost):
    '''Returns True when the payment is accepted, or False if money is insufficient'''
    if payment < drink_cost:
        print("Not enough money")
        return False
    else:
        change = int(payment - drink_cost)
        print(f"Here is {change} Kr in change.")
        global money
        money += drink_cost
        return True

def make_coffee(drink_name, order_ingredient):
    '''Deduct the required ingredients from the stock.'''
    for item in order_ingredient:
        stock[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}🤪.")

money = 0
stock = {
    "sodawater": 50,
    "coffee": 50,
    "thai-tea": 50,
    "bananlikör": 50,
    "bailey": 50,
    "vodka": 50,
    "whiskey": 50
}
is_on = True
while is_on:
    user_input = input("Vad önskas? (gullan, mumman, frugan, beauty, fizz, buzz, report or off): ")


    if user_input == "report":
        print(f"Sodawater: {stock['sodawater']} cl")
        print(f"Coffee: {stock['coffee']} cl")
        print(f"Thai-tea: {stock['thai-tea']} cl")
        print(f"Bananlikör: {stock['bananlikör']} cl")
        print(f"Bailey: {stock['bailey']} cl")
        print(f"Vodka: {stock['vodka']} cl")
        print(f"Whiskey: {stock['whiskey']} cl")
        print(f"Money: {money} SEK")
    elif user_input == "off":
        is_on = False
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredienser"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["pris"]):
                make_coffee(user_input, drink["ingredienser"])
