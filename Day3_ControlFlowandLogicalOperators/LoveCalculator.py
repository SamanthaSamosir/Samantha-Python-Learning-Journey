print("The Love Calculator is calculating your score...")
name1=input("What is your name? ")
name2=input("What is their name? ")
combinedNames=name1+name2
lowerNames=combinedNames.lower()
t=lowerNames.count("t")
r=lowerNames.count("r")
u=lowerNames.count("u")
e=lowerNames.count("e")
firstDigit=t+r+u+e

l=lowerNames.count("l")
o=lowerNames.count("o")
v=lowerNames.count("v")
e=lowerNames.count("e")
secondDigit=l+o+v+e

score=int(str(firstDigit)+str(secondDigit))
if(score<10) or (score>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif(score>=40) and (score<=5>0):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
