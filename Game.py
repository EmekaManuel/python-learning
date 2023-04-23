command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else: 
            started = True
            print("car started...")    
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("car has stopped.")  
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the simaulation
        """)      
    elif command == "quit":
        break
    else: 
        print("enter a valid input")
        
