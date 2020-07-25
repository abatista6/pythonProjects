# Adrianna Batista
# 2/28/2019
# A program thats implements forward chaining of positive Horn clauses in Python


#given example rules

PROPS = ['A', 'B', 'Q', 'R']

rule1 = [[0,1],2] #A and B => Q
rule2 = [[2],0] #Q => A
rule3 = [[],0] #A
rule4 = [[],1] #B

RULES = [rule1, rule2, rule3, rule4]


#function that performs forward chaining
def fchain(PROPS, RULES):

    VALS = [False] * len(PROPS) #generate list of truth values init to False

    CTRS = [] #generate list of rule counters as needed
    
    TRACK = [] #list populated with known true values


    for r in RULES: #generate counters for every rule
        
        CTRS.append(len(r[0]))

        if len(r[0])==0:

            TRACK.insert(0, r[1]) #add values to truth list

    while TRACK:

        pos = TRACK.pop() #pop item index from queue

        if VALS[pos] is False:

            VALS[pos] = True

        tempC = 0 #temp counter

        for r in RULES:
            
            if pos in r[0]:

                CTRS[tempC] -= 1

                if CTRS[tempC] == 0:

                    TRACK.insert(0, r[1]) #add values to truth list

            tempC += 1 #increment temp counter

    #display info to user
    print(PROPS)
    print(VALS)

fchain(PROPS, RULES) #return data