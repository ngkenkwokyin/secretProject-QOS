import random

print("=+=+=+=+=+=+=+= Welcome to Sea Bounty House =+=+=+=+=+=")
option = -1
NumberOfCust = 14

waitingTime = 0
while True:
    print("There are about {} waiting in front of you".format(NumberOfCust))
    print("Today's special: 95% of guests ordered the grilled chicken.")
    print("There will be a discount of about 5% if you spend a minimum of $50")
    option = int(input("Choose your option (0 for exit())"))
    if option == 1:
        if NumberOfCust <= 5:
            waitingTime = 8
            print("The waiting time is 8 minutes")

        elif NumberOfCust <=10:
            waitingTime = 12
            print("The waiting time is 12 minutes")

        elif NumberOfCust <=15:
            waitingTime = 18
            print("The waiting time is 18 minutes")

        elif NumberOfCust <=20:
            waitingTime = 24
            print("The waiting time is 24 minutes")

        elif NumberOfCust <=30:
            waitingTime = 45
            print("The waiting time is 45 minutes")

        elif NumberOfCust <=40:
            waitingTime = 50
            print("The waiting time is about 50 minutes")

        else:
            waitingTime = 60
            print("The waiting time may be longer than an hour")

        
                









