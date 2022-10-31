import random
response = "y"
while response == "y":
    no = random.randint(1,6)
    if(no == 1):
        print("*")
    if(no == 2):
        print("**")
    if(no == 3):
        print("***")
    if(no == 4):
        print("****")
    if(no == 5):
        print("*****")
    if(no == 6):
        print("******")
    response = input("Do you want to roll a dice? Enter y for yes and n for no.")
    print("\n")