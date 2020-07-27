# Adrianna Batista
# 11/30/2018
# Lab#8: Write a python program that reads data from file and uses matplotlib to
#plot a pie chart showing how you spend your money.

import matplotlib.pyplot as plt


def main():

    #variable declaration
    data=""
    lab=""
    temp1=""
    temp2=""
    
    #read line from text file 'data.txt'
    with open("data.txt","r") as file:

        lab = file.readline()

        numStr = file.readline()

        #iterate through word and split char
        for line in lab:
               
            temp1 = lab.split(",")
        
            temp2 = numStr.split(",")

        lab = temp1

    data = temp2
    
    plt.pie(data, labels=lab)

    plt.title("Batista Expenses (Lab #8)")

    plt.show()

main()
