#coffee
print("Welcome to the coffee machine!")
money=0
water=300
milk=200
coffee=100
machine_on=True
def take_money(n):
    global money
    print(f"\nPlease insert {n}$ in the form of coins")
    penny=int(input("\nHow many pennies are you inserting?: "))*0.01
    dime=int(input("How many dimes are you inserting?: "))*0.10
    nickel=int(input("How many nickels are you inserting?: "))*0.05
    quarter=int(input("How many quarters are you inserting?: "))*0.25
    money_given=penny+dime+nickel+quarter
    money_given=round(money_given, 3)
    if money_given==n:
        money+=n
        return print(f"Accepted {n}$\nDrink poured\n")
    elif money_given>n:
        money+=n
        change=round(money_given-n, 4)
        return print(f"{change}$ is your change\nDrink poured\n")
    else:
        return print(f"Not enough money. Money returned")
    
def pour_milk(n):
    global milk
    if milk-n>=0:
        milk-=n
    else:
        return "Not enough milk"
def pour_water(n):
    global water
    if water-n>=0:
        water-=n
    else:
        return "Not enough water"
def add_coffee(n):
    global coffee
    if coffee-n>=0:
        coffee-=n
    else:
        return False
def report():
    print(f"\nWater:{water}ml\nMilk:{milk}ml\nCoffee:{coffee}gm\nMoney:{money}$\n")
def espresso():
    glass=r"""
    (  )
     ) (
   _______

  |       |___
  |  ___  |   |
  |_______|___|
   =======
"""
    add_coffee(18)
    pour_water(50)
    output=take_money(1.50)
    if output!="Not enough money. Money returned":
        print(glass)
def latte():
    glass=r"""
       ( (
        ) )
      .....

     | .'. |
     |'- -'|___
     |     |   |
     |     |___|
      \___/
"""
    add_coffee(24)
    pour_water(200)
    pour_milk(150)
    output=take_money(2.50)
    if output!="Not enough money. Money returned":
        print(glass)
def cappuchino():
    glass=r"""
      (   )
     ( ( ) )
      ) _ (
   .---------.
  /  ~~~~~~~  \___

  |           |   |
  \           /___|
   `---------'
     =======
"""
    add_coffee(24)
    pour_water(250)
    pour_milk(100)
    output=take_money(3)
    if output!="Not enough money. Money returned":
        print(glass)
def machine():
    global machine_on
    while machine_on==True:
        choice=input("What would you like to have? An Espresso? Latte? or a Cappuchino?" \
        "\nOr would you like an inventory report? For report, type in 'report'?: ").lower()
        if choice=="espresso":
            espresso()
        elif choice=="latte":
            latte()
        elif choice=="cappuchino":
            cappuchino()
        elif choice=="report":
            report()
        elif choice=="off":
            machine_on=False
        else:
            print("Make sure you gave a proper input")  
machine()