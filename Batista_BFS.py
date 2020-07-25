#Adrianna Batista
#2-7-2019
#Breadth-first search of jugs, gallons, and water faucet 

# Initial State
jugs = [0,0,0]


def findSolution(jugsS):
    # jugs[0] = 12G
    # jugs[1] = 8G
    # jugs[2] = 3G


    # Keep track of visited nodes
    visited = []

    # path/s to solution
    paths = []


    paths.append(jugsS)
    #visited.append(jugsS)


    while len(paths) > 0:


            jugs = paths.pop(0)


            if(1 in jugs):

                break

            # fill 12
            if jugs[0] < 12:
                # fill jug

                if jugs[0] == 0:
                    jugs[0] = 12
                    #findSolution(jugs)
                    if jugs not in visited:
                        visited.append(jugs)
                        paths.append(jugs)



                # empty 12 into 8
                if jugs[0]+jugs[1] <= 8:
                    jugs[1] += jugs[0]
                    jugs[0] = 0
                    #findSolution(jugs)


                    if jugs not in visited:
                        visited.append(jugs)
                        paths.append(jugs)

                # fill whatever can
                else:
                    rem = 8-jugs[1]
                    jugs[0] -= rem
                    jugs[1] += rem
                    #findSolution(jugs)

                    if(jugs not in visited):
                        visited.append(jugs)
                        print(visited)
                        paths.append(jugs)

                # empty 12 into 3
                if(jugs[0]+jugs[2] <= 3):
                    jugs[2] += jugs[0]
                    jugs[0] = 0
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)

                # fill whatever can
                else:
                    rem = 3-jugs[2]
                    jugs[0] -= rem
                    jugs[2] += rem
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        print(visited)
                        paths.append(jugs)
            else:
                jugs[0] = 0
                #findSolution(jugs)
                if(jugs not in visited):
                    visited.append(jugs)
                    paths.append(jugs)


            # fill 8
            if(jugs[1] < 8):
                # fill jug
                if(jugs[1] == 0):
                    jugs[1] = 8
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)

                # empty 8 into 12
                if(jugs[1]+jugs[0] <= 12):
                    jugs[0] += jugs[1]
                    jugs[1] = 0
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)

                # fill whatever can
                else:
                    rem = 12-jugs[0]
                    jugs[1] -= rem
                    jugs[0] += rem
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)

                # empty 8 into 3
                if(jugs[1]+jugs[2] <= 3):
                    jugs[2] += jugs[1]
                    jugs[1] = 0
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)
                # fill whatever can
                else:
                    rem = 3-jugs[1]
                    jugs[1] -= rem
                    jugs[2] += rem
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)
            else:
                jugs[1] = 0
                #findSolution(jugs)
                if(jugs not in visited):
                    visited.append(jugs)
                    paths.append(jugs)


            # fill 3
            if(jugs[2] < 3):
                # fill jug
                if(jugs[2] == 0):
                    jugs[2] = 3
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)

                # empty 3 into 12
                if(jugs[2]+jugs[0] <= 12):
                    jugs[0] += jugs[2]
                    jugs[2] = 0
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)
                # fill whatever can
                else:
                    rem = 12-jugs[0]
                    jugs[2] -= rem
                    jugs[0] += rem
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)

                # empty 3 into 8
                if(jugs[2]+jugs[1] <= 8):
                    jugs[1] += jugs[2]
                    jugs[2] = 0
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)
                # fill whatever can
                else:
                    rem = 8-jugs[1]
                    jugs[2] -= rem
                    jugs[1] += rem
                    #findSolution(jugs)
                    if(jugs not in visited):
                        visited.append(jugs)
                        paths.append(jugs)
            else:
                jugs[2] = 0
                #findSolution(jugs)
                if(jugs not in visited):
                    visited.append(jugs)
                    paths.append(jugs)



findSolution(jugs)