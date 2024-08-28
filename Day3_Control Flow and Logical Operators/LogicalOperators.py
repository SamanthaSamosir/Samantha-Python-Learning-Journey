print("Welcome to the rollercoaster!")
bill=0
height=int(input("What is your height in cm? "))
if height>=120:
    print("You can ride the rollercoaster!")
    age=int(input("What is your age? "))
    if age<=12:
        bill=35000
        print("Please pay Rp35,000,-")
    elif age<=18:
        bill=55000
        print("Please pay Rp55,000,-")
    #update here ya
    elif age>=45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us.")
    else:
        bill=129000
        print("Please pay Rp129,000,-")
    wants_photo=input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo=="y":
        bill+=15000
    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
