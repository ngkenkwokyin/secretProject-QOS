import random
from datetime import datetime, timedelta # timedelta for time difference
from time import sleep

print("=+=+=+=+=+=+=+= Welcome to Sea Bounty House =+=+=+=+=+=+=+=")
option = -1
NumberOfCust = 14 #test data, can be ported from API

waitingTime = 0
table_status = "Not ready"
ready_time = None
extra_time = None

def waiting_status():
    global waitingTime
    global ready_time
    global extra_time
    global table_status

    choice = input("Do you want to wait for your table? (yes/no): ").lower()

    if choice == "yes":
        if ready_time is None:
            ready_time = datetime.now() + timedelta(minutes=waitingTime)
            

        elif datetime.now() >= ready_time:
            print("🟡 Preparing your table")

        else:
            print("🔴 You are still in the queue")

        if table_status == "Preparing your table":
                sleep(600) # 10 minustes
                extra_time = timedelta(minutes=10)
                ready_time += extra_time
                table_status = "Your table is ready"
        if table_status == "Your table is ready":
                print("🟢 Your table is ready")

    elif choice == "no":
        print("Returning to main menu...")
        return main_menu()
    

def main_menu():
    while True:
        print()
        print()
        print("==== WAITING INFORMATION ====")
        print("There are about {} people queuing in front of you".format(NumberOfCust))
        print()
        print()
        print("====== Discounts and Restaurant Insights =====")
        print("Today's special: 95% of guests ordered the grilled squid.")
        print("There will be a discount of about 5% if you spend a minimum of $50")
        print("First 20 customers will have a free ice-cream!")
        print()
        print()
        print("================ SELECT YOUR OPTION ================")
        print("Type 0 for exit the QOS terminal system, Type 1 for waiting status, Type 2 for soup of the day")
        option = int(input("Choose your option (0 for exit())"))
        if option == 0:
            #break
            exit()
        if option == 1:
            waiting_status()
            if NumberOfCust <= 5:
                waitingTime = 8
                print("The waiting time is 8 minutes")
                print("🔴 You are still in the queue")
                ready_time = datetime.now() + timedelta(minutes=8)
                while datetime.now() < ready_time:
                    sleep(1) #count per second
                
                table_status = "Preparing your table"
                print("🟡 Preparing your table")
                sleep(600) # 10 mins
                print("🟢 Your table is ready")
                table_status = "Your table is ready"


            elif NumberOfCust <=10:
                waitingTime = 12
                print("The waiting time is 12 minutes")
                print("🔴 You are still in the queue")
                ready_time = datetime.now() + timedelta(minutes=12)
                while datetime.now() < ready_time:
                                sleep(1)
                table_status = "Preparing your table"
                print("🟡 Preparing your table")
                sleep(600)
                print("🟢 Your table is ready")
                table_status = "Your table is ready"
                
                

            elif NumberOfCust <=15:
                waitingTime = 18
                print("The waiting time is 18 minutes")
                print("🔴 You are still in the queue")
                ready_time = datetime.now() + timedelta(minutes=18)
                while datetime.now() < ready_time:
                                            sleep(1)
                table_status = "Preparing your table"
                print("🟡 Preparing your table")
                sleep(600) 
                print("🟢 Your table is ready")
                table_status = "Your table is ready"

            elif NumberOfCust <=20:
                waitingTime = 24
                print("The waiting time is 24 minutes")
                print("🔴 You are still in the queue")
                ready_time = datetime.now() + timedelta(minutes=18)
                while datetime.now() < ready_time:
                                            sleep(1)
                print("🟡 Preparing your table")
                sleep(600) 
                print("🟢 Your table is ready")
                table_status = "Your table is ready"

            elif NumberOfCust <=30:
                waitingTime = 45
                print("The waiting time is 45 minutes")
                print("🔴 You are still in the queue")
                ready_time = datetime.now() + timedelta(minutes=45)
                while datetime.now() < ready_time:
                                            sleep(1)
                print("🟡 Preparing your table")
                sleep(600) 
                print("🟢 Your table is ready")
                table_status = "Your table is ready"

            elif NumberOfCust <=40:
                waitingTime = 50
                print("The waiting time is about 50 minutes")
                print("🔴 You are still in the queue")
                ready_time = datetime.now() + timedelta(minutes=50)
                while datetime.now() < ready_time:
                                            sleep(1)
                table_status = "Preparing your table"
                print("🟡 Preparing your table")
                sleep(600)
                print("🟢 Your table is ready")
                table_status = "Your table is ready"

            else:
                waitingTime = 60
                print("The waiting time may be longer than an hour")
                print("🔴 You are still in the queue")
                ready_time = datetime.now() + timedelta(minutes=60)
                while datetime.now() < ready_time:
                                            sleep(1)
                table_status = "Preparing your table"
                print("🟡 Preparing your table")
                sleep(600)
                print("🟢 Your table is ready")
                table_status = "Your table is ready"
        

        if option == 2:
                print("========THE SOUP OF THE DAY=======")
                today = datetime.today().weekday()
                if today % 7 == 0:
                    print("The soup of the day is tomato soup")
                elif today == 1:
                    print("The soup of the day is calm soup")
                elif today == 2:
                    print("The soup of the day is seafood soup")
                elif today % 3 == 0:
                    print("The soup of the day is miso soup")
                elif today == 4:
                    print("The soup of the day is vegetable soup")
                elif today == 5:
                    print("The soup of the day is tofu soup")
                else:
                    print("The soup of the day is beef stew")
                print()
                print()
        else:
                print()
                print()
                print("===== ERROR MESSAGE =====")
                print("Invalid Option")
                continue
        

#start the program
main_menu()
        
                



