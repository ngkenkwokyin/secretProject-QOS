import random
from datetime import datetime, timedelta # timedelta for time difference
from time import sleep
import secrets #make it secure so people wont abuse generate fake codes, cryptography included
import string
import os
points = 0 

print("=+=+=+=+=+=+=+= Welcome to Sea Bounty House =+=+=+=+=+=+=+=")
option = -1
NumberOfCust = 14 #test data, can be ported from API

waitingTime = 0
table_status = "Not ready"
ready_time = None #save ready time info
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
    
def generate_voucher():
    chars = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(8))

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
        print("\nType 0 for exit the QOS terminal system\t \noption 1 for waiting status\t \noption 2 for soup of the day\t \noption 3 for Game 1\t \noption 4 for Game 2\t \noption 5 for game points & rewards \n")
        option = int(input("Choose your option (0 for exit())"))
        global points
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
        

        elif option == 2:
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

        elif option == 3:
                while True:
                    print("==== ROCK PAPER SCISSORS ==== ")

                    choice = ['rock', 'paper', 'scissors']
                    machine_choice = random.choice(choice)

                    your_choice = input("choose your pick (rock, paper, scissors)").lower()

                    if your_choice == machine_choice:
                            print('Draw')
                            print("You chose:", your_choice)
                            print("Machine chose:", machine_choice)
                            points += 1
                            print("You have earned one point.")
                    elif (your_choice == "rock" and machine_choice == "scissors") or \
                        (your_choice == "paper" and machine_choice == "rock") or \
                        (your_choice == "scissors" and machine_choice == "paper"):
                        print("You win!")
                        print("You chose:", your_choice)
                        print("Machine chose:", machine_choice)
                        points += 3
                        print("You have earned 3 points")

                    else:
                            print("Computer win")
                            print("You have earned 0 points")

# validation checks
                    if your_choice not in choice:
                            print("Invalid input")
                            continue

                    exit_choice = input("Do you want to exit this game? (yes/no): ").lower()

                    if exit_choice == "yes":
                            break
                    else:
                            continue
                  
        elif option == 4:
                while True:
                    y = random.randint(1,12)
                    z = random.randint(1,10)
                    print("===== TIMES TABLE GAME =====")
                    print("Note: You are to only be allowed to enter a number")
                    prompt_input = input("What is {} × {}? ".format(y,z))
                    if not prompt_input.isnumeric():
                                            print("Invalid format")
                    answer = int(prompt_input) 
                    answer_key = y * z
                    if answer == answer_key:
                            print("Well done! You got it right!")
                            print("You got a point")
                            points += 1
                    else:
                            print("You got it wrong!")
                            print("No points awarded")

                    exit_choice = input("Do you want to exit this game? (yes/no): ").lower()
                    
                    if exit_choice == "yes":
                            break


        elif option == 5:
                print()
                print()
                print("======= GAME POINTS AND REWARD SYSTEM =======")
                print("You have {} points".format(points))

                if points > 5:
                        print("You have a free ice-cream")
                        print("Remember to take a screenshot in case you lose your progress!")
                        generate_voucher()
                        voucher = generate_voucher()
                        print("Your voucher is: ", voucher)


                if points > 30:
                        print("You have a free ice-cream and a free drink")
                        print("Remember to take a screenshot in case you lose your progress!")
                        generate_voucher()
                        voucher = generate_voucher()
                        print("Your voucher is: ", voucher)
                


               



    



        else:
                print()
                print()
                print("===== ERROR MESSAGE =====")
                print("Invalid Option")
                continue
        

#start the program
main_menu()
        
                



