print("Welcome to the rollercoaster!")
bill=0
height=int(input("What is your height in cm? "))
if height>=120:
    print("You can ride the rollercoaster!")
    age=int(input("What is your age? "))
    if age<=12:
        print("Please pay Rp35,000,-")
    elif age<=18:
        print("Please pay Rp55,000,-")
    else:
        print("Please pay Rp129,000,-")
else:
    print("Sorry, you have to grow taller before you can ride.")
