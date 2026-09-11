inv = []
quit = 0

while quit == 0:
    info = input("Please enter stock quantity:")
    if info == "quit":
        print ("Thank you for updating")
        print ("Here is the total:", total)
        break
    elif (info.isdigit()) == True:
        new_info = int(info)
        if new_info < 0:                                                #  Omit - values
            print (new_info)
            print ("Try again")
            failed +=1                                               # Failed/rejected inputs
        else:                                                        #  Manage state [Update the inv list]
            inv.append(new_info)
            print (inv)                                              #  Show user list
            int_inv = list(map(int, inv)) 
            total = sum(int_inv) 
            if total > 500 :
                print ("Overstock Alert")  
                print ("Thank you for updating")
                print ("Here is the total:", total)                                  
        print ("Accepted")     
    else:
        print ("Rejected/invalid Input")                              