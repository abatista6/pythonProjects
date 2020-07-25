# Adrianna Batista
# 10/5/18
# Write a program for airlines to allow the customer to purchase flights and perform calculations

ansCheck=False
ansFlag=False
ansOkay=False
ansTrue=False
dayTime=False
weekDay=False

cost=float(0)

#Display program welcome
print("\n********************************************************")
print("                    W E L C O M E   T O                ")
print("\n                 A V B  A I R L I N E S              ")
print("*********************************************************")


#Prompt user for data input
while not ansCheck:
    dest=str(input("\n What is your destination? Enter [C]hicago, [M]iami, or [P]ortland: "))
    if (dest == "C" or dest == "c" or dest == "M" or dest == "m" or dest == "P" or dest == "p"):
        ansCheck=True
    else:
        print("\n ERROR! Invalid entry, try again")
           
while not ansFlag:
    travelTime=int(input("\n What is you travel time? (Enter time between 0000-2359): "))
    if ((travelTime >= 0 and travelTime < 24) or (travelTime >= 100 and travelTime < 2400)):
        ansFlag=True
        if ((travelTime >= 500 and travelTime <= 1900)or(travelTime >= 5 and travelTime <= 19)):
            dayTime=True
        elif ((travelTime < 500 and travelTime > 1900) or (travelTime < 5 and travelTime > 19)):
            dayTime=False
    else:
        print("\n ERROR! Invalid entry, try again")
    
while not ansOkay:
    dayType=str(input("\n What type of day are you traveling? (week[E]nd or week[D]ay): "))
    if (dayType == "E" or dayType == "e"):
        ansOkay=True
        weekDay=False
    elif (dayType == "D" or dayType == "d"):
        ansOkay=True
        weekDay=True
    else:
        print("\n ERROR! Invalid entry, try again")

#Perform ticket calculations based on data

#Miami Tickets
if(dest=="M" or dest=="m"):
    #Weekday flight
    if weekDay:
        #Daytime flight
        if dayTime:
            cost=150
        #Nighttime flight
        else:
            cost=100
    #Weekend flight
    else:
        #Daytime flight
        if dayTime:
            cost=180
        #Nighttime flight
        else:
            cost=120

#Chicago Tickets
elif(dest=="C" or dest=="c"):
    #Weekday flight
    if weekDay:
        #Daytime flight
        if dayTime:
            cost=75
        #Nighttime flight
        else:
            cost=50
    #Weekend flight
    else:
        #Daytime flight
        if dayTime:
            cost=90
        #Nighttime flight
        else:
            cost=60
            
#Portland Tickets
elif(dest=="P" or dest=="p"):
    #Weekday flight
    if weekDay:
        #Daytime flight
        if dayTime:
            cost=300
        #Nighttime flight
        else:
            cost=200
    #Weekend flight
    else:
        #Daytime flight
        if dayTime:
            cost=360
        #Nighttime flight
        else:
            cost=240

#Output cost calculation
print("\n Each ticket will cost: $%s" % format(cost, ".2f"))

#Prompt user for data
qty=int(input("\n Enter amount of tickets desired: "))
if(qty>=1):
    ansTrue=True
else:
    print("\n ERROR: Invalid ticket entry! Your order has been cancelled")
    print("\n The program will end now...Good bye.")
    exit()

#Calculate total
total=cost*qty

#Output total calculation
print("\n You owe: $%s" % format(total,".2f"))

#Get user input
pay=float(input("\n Enter the amount you will pay: $"))
if(pay>=total):
    temp=pay-total
    print("\n You will get $%s in change" % format(temp,".2f"))
    print("\n Your tickets have been ordered! Thanks for traveling with AVB Airlines")
else:
    print("\n ERROR: Insufficient funds! No tickets ordered.")
    print("\n The program will end now...Good bye.")
    exit()
