print("Thank you for choosing Samantha's Pizza Deliveries!")
size=input("What size of pizza do you want? (S/M/L) ")
addPepperoni=input("Do you want pepperoni? (Y/N) ")
extraCheese=input("Do you want an extra cheese? (Y/N) ")
#psst this is in IDR or Indonesian Rupiah ya :D
bill=0
if size=="S":
    bill+=15000
elif size=="M":
    bill+=20000
else:
    bill+=29000
if addPepperoni=="Y":
    if size=="S":
        bill+=29000
    else:
        bill+=35000
if extraCheese=="Y":
    bill+=9000
print(f"Your final bill is Rp{bill}")
