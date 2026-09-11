inv = []
quit = 0

while quit == 0:
    info = input("Please enter stock quantity:")
    if info == "quit":
        print ("Thank you for updating")
        break
    elif (info.isdigit()) == True:
        new_info = int(info)    
        print ("Accepted")     
    else:
        print ("Rejected/invalid Input")                              