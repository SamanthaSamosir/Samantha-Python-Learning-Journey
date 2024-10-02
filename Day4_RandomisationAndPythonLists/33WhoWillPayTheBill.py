#Who will pay the bill?
import random
#use choice for sequence
friends = ["Samantha", "Lisa", "Yola", "Ridho", "Andi", "Rei"]
#option1
ran = random.choice(friends)
print(ran)
print(random.choice(friends))

#option2
random_index = random.randint(0,len(friends))
print(friends[random_index])