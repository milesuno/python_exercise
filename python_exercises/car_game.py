# Working with while loops and conditional statements
exit = False
car_on = False

while exit == False:
    user_input = input("Enter command: ").upper()
    print(f"user entered{user_input}")

    if user_input == "HELP":
        print(
            """
Welcome to the help panel, you have the following options:
            
Start: To start Car.
            
Stop: To stop Car.
            
Quit: To exit Car game.
            """)

    elif user_input == "START":
        if car_on:
            print("Car is already running")
        else:
            car_on = True
            print('"VROOOM!" - You have started the Car')



    elif user_input == "STOP":
        if not car_on:
            print("Car is already off")
        else:
            car_on = False
            print("*Click* - Car stopped")


    elif user_input == "QUIT":
        print("Car game ended")
        exit = True

    else:
        print("I don't understand that command. They typing 'Help'.")