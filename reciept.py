# Adrianna Batista
# September 14, 2018
# CISC 2500: Information and Data Managemnet
# Python Lab #1: program outputs reciept information to terminal output device

from __future__ import print_function

#variable declaration and assignment
price1 = 1.49 #floating number price of first product (orange)
price2 = 0.69 #floating number price of second product (bagels)
saletotal = price1 + price2 #floating number sale subtotal
saletax = 0.11 #floating number price of sales tax
total = saletotal + saletax #floating number total price of sale
given = 5.00 #floating number of cash amount given
change = given - total #floating number of change amount to be given

#reciept display information
print("\n          WELCOME TO SCHNUCKS")
print("             RICHMOND CENTER \n")
print("             The Friendliest")
print("             Stores in Town")
print("              314-644-0510")
print(" --------------------------------------")
print("  SIMP ORANGE ORIG SNGL    t F    %s " % (price1))
print("  BAGELS                   t F    %s " % (price2))
print("  BAGELS                   t F    ", price2)

print(" ********** Sale Subtotal***   %s " % (saletotal))
print("      SALES tax-LO     %s " % (saletax))
print(" ************** Total Sale***    %s " % (total))
print("  *** CASH                        %.2f" % (given))
print("         Change:    %s   $" % (change))    
print(" **************************************")
print(" Reciept Required for Refunds/Exchanges")
print(" **************************************")
print("  Your Cashier: USCAN 374")
print(" --------------------------------------")
print("                 Visit Us")
print("                On-line at")
print("             www.schnucks.com")
print("              Store Manager -")
print("              Jerry Lueders \n")
print("  483007 01-24-11  8:35A 374/04/0272 \n")

#End of program

