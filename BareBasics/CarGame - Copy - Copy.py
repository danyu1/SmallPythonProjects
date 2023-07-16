command = ""
started = False
stopped = True
while (command.lower () != "quit"):
    command = input ("> ").lower ()
    if (command == "quit"):
        break
    elif (command == "stop" and stopped == False):
        print ("Car stopped.")
        stopped = True
        started = False
    elif (command == "stop"):
        print ("Car already stopped")
    elif (command == "start" and started == False):
        print ("Car started... Ready to go!")
        started = True
        stopped = False
    elif (command == "start"):
        print ("Car already started")
    elif (command == "help"):
        print ('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    else:
        print ("Sorry enter a valid input!")
        

