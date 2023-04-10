import random

total = 0
for i in range(6):
	randomvalue = random.random() * 100
	print(f"{i + 1} try : {randomvalue:.2f}")
	total += randomvalue

print(f"you will have {total/6:.2f}% chance to success.")
