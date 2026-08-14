import random


print("SELECT Y for yes \nSELECT N for no")
print("You may win points that can exchange for a free ice cream if you play this game while waiting")
continue_input = input("Do you want to play a game? (Y/N)").upper()


char_list = ["Member", "Imposter", "Sheriff", "Survivor"]

if continue_input == "Y":
    print("\t\t\t ===== NEW GAME ===== \t\t\t")
    print("\n Type the full name of the role: \n Memeber \n Imposter \n Sheriff \n Survivor")
    user_input = input("What is the role you choose: ").capitalize()
    if user_input not in char_list:
        print("\t\t\t ===== ERROR MESSAHE ===== \t\t\t")
        print("Invalid role.")
    else:
        computer_pick = random.choice(char_list)
        print("The mysterious user joined the game.")
        print("The mysterious user has picked a role.")
        print("SELECT Y for yes \nSELECT N for no")
        if user_input != "Sheriff" and user_input != "Imposter":
            new_user_input = input("Do you think the mysterious user is an imposter ? (Y/N)").upper()
            if computer_pick != "Imposter" and new_user_input == "N":
                print("You won!")
                print("You won a free ice cream.")
                #voucher code HERE
            elif computer_pick == "Imposter" and new_user_input == "Y":
                print("You won!")
                print("You won a free ice cream.")
                #voucher code HERE
            else:
                print("You lost! 😭")

            print("Your role: ", user_input)
            print("mysterious user role: ", computer_pick)

        if user_input == "Imposter":
                print("Night falls....")
                new_user_input = input("Do you want to kill the mysterious user  ? (Y/N)").upper()
                if computer_pick != "Imposter" and new_user_input == "N":
                    print("The mysterious man lives...")
                    print("He have suspected you and you have lost... 😭")
                elif computer_pick == "Imposter" and new_user_input == "Y":
                    print("Oops.... you killed your friend... 😭")
                    print("You have officially lost")
                elif computer_pick != "Imposter" and new_user_input == "Y":
                    print("You have decided to kill the mysterious man....")
                    print("His blood is in your hands....")
                    print("BUT you have officially won!")
                    print("Slient win....")
                    #voucher code HERE
                print("Your role: ", user_input)
                print("mysterious user role: ", computer_pick)

                
                

        if user_input == "Sheriff":
            print("Night falls....")
            print("You have 3 bullets.")
            print("SELECT Y for yes \nSELECT N for no")
            new_user_input = input("Do you want to shoot the mysterious user  ? (Y/N)").upper()
            if computer_pick != "Imposter" and new_user_input == "N":
                print("You won!")
                print("You have saved an innocent man.")
                print("You won a free ice cream.")
                #voucher code HERE
            elif computer_pick == "Imposter" and new_user_input == "Y":
                print("You won!")
                print("You have elimated the threat.")
                print("You won a free ice cream.")
                #voucher code HERE
            elif computer_pick != "Imposter" and new_user_input == "Y":
                print("You lost! 😭")
                print("YOU HAVE KILLED AN INNOCENT MAN.")
            else:
                print("You lost! 😭")
                print("THE MYSTERIOUS USER HAS ESCAPED...")
            print("Your role: ", user_input)
            print("mysterious user role: ", computer_pick)


        




        


        

           
            


        