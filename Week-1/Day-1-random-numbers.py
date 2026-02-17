import random 

number = random.randint(1,10)
print(f"Your number is: {number}")

while True :
    ans = input("Do you want to generate a casual number? ").lower()
    if ans == "y" :
        number = random.randint(1,10)
        print(number)
    else :
        print("Goodbye!")
        break