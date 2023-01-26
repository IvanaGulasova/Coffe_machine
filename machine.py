from source_data import MENU
from source_data import resources
from choice_text import text

section = "-" * 40
coffee_maker_prepares = True

def check_resources(cafe):
    return hasResources("water") and hasResources("milk") and hasResources("coffee")
    
def hasResources(ingredient):
    return (resources[ingredient] - MENU[cafe]["ingredients"][ingredient]) >= 0
    
def actual_materials(cafe):
    resources["water"] = resources["water"] - MENU[cafe]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[cafe]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[cafe]["ingredients"]["coffee"]
    return resources

def paymant(cafe):
    price_coffee = MENU[cafe]["cost"]

    while True:
        try:
            crown_1 = int(input("How many 1Kc do you want to deposit: "))
            crown_2 = int(input("How many 2Kc do you want to deposit: "))
            crown_5 = int(input("How many 5Kc do you want to deposit: "))
            crown_10 = int(input("How many 10Kc do you want to deposit: "))
            crown_20 = int(input("How many 20Kc do you want to deposit: "))
            crown_50 = int(input("How many 50Kc do you want to deposit: "))
            break
        except ValueError:
            print("Only numbers can be entered, please try again..")
           
    print(section)
        
    sum = crown_1 * 1 + crown_2 * 2 + crown_5 * 5 + crown_10 * 10 + crown_20 * 20 + crown_50 * 50
    if sum < price_coffee:
        print("Lack of money..I'm refunding the money and ending the program.\n")
        quit()
    print(f"Deposit: {sum}Kc")
    if sum > price_coffee:
        back_money = sum - price_coffee
        print(f"Returnd: {back_money}Kc")
        print(section)
    elif sum == price_coffee:
        print("You have deposited the exact amount.")
        print(section)
    
def choose_cafe(cafe):
    if choose == "latte":
        cafe = "latte"
    elif choose == "espresso":
        cafe = "espresso"
    elif choose == "cappuccino":
        cafe = "cappuccino"
        

def total_price(cafe):
    if choose == "latte":
        price = MENU[cafe]["cost"]
    elif choose == "espresso":
        price = MENU[cafe]["cost"]
    elif choose == "cappuccino":
        price = MENU[cafe]["cost"]
    return price


while coffee_maker_prepares:
    print(text)
    # print(f"Current status of resources: {resources}\n")
    choose = input("What kind of coffee do you want\n >>>  ").lower()
    if choose == "report":
        print(resources)
        quit()
    
    cafe = choose
    price = total_price(choose)
    finnal_check = check_resources(cafe)

    if finnal_check == False:
        print("We don't have enough raw materials, sorry..")
        quit()
    
    actual = actual_materials(cafe)
    # print(f"The rest of the resources: {resources}")
    print(f"The {cafe} costs {price} crowns.")
    print(section)

    paymant(cafe)
    print("The coffee is prepared..")
    print(section)

    while True:
        next_order = input("Do you want to buy another coffee?\n yes/no >>> ")
        if next_order == "yes":
            break
        else:
            print("Enjoy your coffee.\nWe look forward to the next time")
            print(section)
            quit()

