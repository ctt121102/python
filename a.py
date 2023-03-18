#gpa = 5.8
#distance = 4.2
#price = gpa * distance 
#print(f"Your gpa is {gpa}")
#print(f"Your distance is {distance}Km")
#print(f"Your price is ${price}")

#Name = input("Enter your name: ")
#Food = input("Enter your food: ")
#Email = input("Enter your email: ")
#print(f"Hello: {Name}")
#print(f"You called: {Food}")
#print(f"Your email is: {Email}")

#item = input("What item would you like to buy: ")
#price = float(input("What is the price ($): "))
#quantity = int(input("How many would you like: "))

#Total = price * quantity
#print(f"You have bought {quantity} x {item}")
#print(f"Your total is: ${round(Total, 2)}")

#import math
#x = 25.1
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)
#import math
#print("A = pi * r^2")
#radius = float(input("Enter the radius of a cirle: "))
#A = math.pi * pow(radius, 2)
#print(f"A = {round(A, 2)}cm^2")

#age = int(input("Enter your age: "))
#if age >= 100:
#    print("you are too old to sign up!")
#elif age >= 18:
#    print("your are young!")
#elif age < 0:
#    print("You haven't been born yet!")
#else:
#    print("You are kid!")

#online = False
#if online:
#    print("The user is online")
#else:
#    print("The user is offline")

#calc = input("Enter a calculator (+ - * /): ")

#num1 = float(input("Enter the 1st numer: "))
#num2 = float(input("Enter the 2nd numer: "))

#if calc == "+":
    #result = num1 + num2
    #print(round(result, 3))
#elif calc == "-":
    #result = num1 - num2
    #print(round(result, 3))
#elif calc == "*":
    #result = num1 * num2
    #print(round(result, 3))
#elif calc == "/":
    #result = num1 / num2
    #print(round(result, 3))
#else:
    #print(f"{calc} is not a valid")

#a = input("nhập ký tự: ")
#i = 1
#while True:
#    i = i + 1
#    print(f"{i}. {a}")

#unit = input("Enter this temperature in Celsius or Fahrenheit (C/F): ")   #CT: C = (temp * 9) / 5 + 32             #BT
#temp = float(input("Enter the tempurature: "))
#if  unit == "C":
#    temp = round((temp * 9) / 5 + 32, 2)
#    print(f"The tempurature in Fahrenheit is: {temp}°F")
#elif unit == "F":
#    temp = round((temp - 32) * 5 / 9, 2)
#    print(f"The tempurature in Celius is: {temp}°C")
#else:
#    print(f"{unit} is an invalid unit of measurement")

#username = input("Enter your username: ")                                    #BT
#if len(username) > 12:
#    print("Your username can't be more than 12 characters")
#elif not username.find(" ") == -1:
#    print("Your username can't contain spaces")
#elif not username.isalpha():
#    print("Your username can't contein numbers")
#else:
#    print(f"Welcome {username}")

#age = int(input("Enter your age: "))                                          #BT
#while age < 0:
#    print(f"Age can't be negative")
#    age = int(input("Enter your age: "))
#print(f"You are {age} years old")

#principle = 0                                                                 #BT
#rate = 0
#time = 0
#while True:
#    principle = float(input("Enter the principle amount (Tiền Gốc): "))
#    if principle <= 0:
#        print(f"Principle can't be less than or equal to zero")
#    else:
#        break
#while True:
#    rate = float(input("Enter the interest rate (Lãi Suất): "))
#    if rate <= 0:
#        print(f"Interest rate can't be less than or equal to zero")
#    else:
#        break
#while True:
#    time = float(input("Enter the time years (Thời Gian): "))
#    if time <= 0:
#        print(f"Time can't be less than or equal to zero")
#    else:
#        break
#Total = principle * pow((1 + rate / 100), time)
#print(f"Balance after {time} years is (Tổng): ${Total:.2f}")

#rows = int(input("Enter the # of rows (Hàng): "))                              #BT
#columns = int(input("Enter the # of colums (Cột): "))
#symbol = input("Enter a symbol to use: ")
#for x in range(rows):
#    for y in range(columns):
#        print(symbol, end="")
#    print()

#import time
#my_time = int(input("Enter the time in seconds: "))
#for x in range(my_time, 0, -1):
#    seconds = x % 60
#    minutes = int(x / 60) % 60
#    hours = int(x / 3600) % 24
#    print(f"{hours:02}:{minutes:02}:{seconds:02}")
#    time.sleep(1)
#print("Waky waky convo Súng!")

#foods = []                                                                     #BT
#prices = []
#total = 0
#while True:
#    food = input("Enter a food to buy (q to quit): ")
#    if food.lower() == "q":
#        break
#    else:
#        price = float(input(f"Enter the price of {food}: $"))
#        foods.append(food)
#        prices.append(price)
#print("----- YOUR CART -----")
#for food in foods:
#    print(food)
#for price in prices:
#    total += price
#print(f"Your total is: ${total}")

#num_pad = ((1, 2 ,3),                                                           #BT
#           (4, 5, 6),
#           (7, 8, 9),
#           ("*", 0, "#"))
#for row in num_pad:
#    for num in row:
#        print(num, end=" ")
#    print()

#a = float(input("Nhap so thap phan a: "))                                       #BT format, round
#b = int(input("làm tròn đến số thứ: "))
#print('format: {0:.{1}f}'.format(a, b))
#formatnum = round(a, b)
#print(f"Round: {formatnum}")

#Nhapdayso = input("Nhập dãy số cách nhau bởi khoảng trắng: ")
#danhsachgiatri = (Nhapdayso.split())
#Danhsachso = map(int, danhsachgiatri)
#Tong = sum(Danhsachso)
#print(f"Tổng dãy số là: {Tong}")

#menu = {"pizza": 3.0,
#        "hotdog": 2.0,
#        "sanwich": 5.2,
#        "hamberger": 7.5,
#        "soda": 2.3,
#        "convo Sung": 1.0}
#cart = []
#total = 0
#print("---------- MENU ----------")
#for key, value in menu.items():
#    print(f"{key:10}: ${value:.2f}")
#print("--------------------------")
#while True:
#    food = input("Select food in menu (q to quit): ").lower()
#    if food == "q":
#        break
#    elif menu.get(food) is not None:
#        cart.append(food)
#print("-------- Your Order --------")
#for food in cart:
#    total += menu.get(food)
#    print(food, end=" ")
#print()
#print(f"Your total is: {total}")


#import random
#options = ("Búa", "Bao", "Kéo")
#player = None
#computer = random.choice(options)
#running = True
#while running:
#    player = None
#    computer = random.choice(options)
#    while player not in options:
#        player = input("Chọn (Búa, Bao, Kéo): ").capitalize()
#    print(f"Player: {player}")
#    print(f"Computer: {computer}")
#    if player == computer:
#        print("Hòa!")
#    elif player == "Búa" and computer == "Kéo":
#        print("Bạn thắng!")
#    elif player == "Bao" and computer == "Búa":
#        print("Bạn thắng!")
#    elif player == "Kéo" and computer == "Bao":
#        print("Bạn thắng!")
#    else:
#        print("Bạn thua!")
#    if not input("Bạn có muốn chơi lại? (y/n): ").lower() == "y":
#        break
#print("Thanks for playing!")

#def get_phone(country, area, first, last):
#    return f"{country}-{area}-{first}-{last}"
#phone_num = get_phone(country=84, area=9, first=17821, last=1810)
#print(phone_num)


nb = [10, 100, 20, 17, 123]
max_value = max(nb)
print(max_value)

min_value = min(nb)
print(min_value)

