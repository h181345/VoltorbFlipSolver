
##    n = 8
##    1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
##    2 + 1 + 1 + 1 + 1 + 1 + 1
##    2 + 2 + 1 + 1 + 1 + 1
##    2 + 2 + 2 + 1 + 1
##    2 + 2 + 2 + 2
##    3 + 1 + 1 + 1 + 1 + 1
##    3 + 2 + 1 + 1 + 1
##    3 + 2 + 2 + 1
##    3 + 3 + 1 + 1
##    3 + 3 + 2

def printer(a_list):
    for n in range(len(a_list)):
        print(a_list[n])
        

def list_with_1s(length):
    # Create an empty list
    numberlist = []
    # Iterate over sequence of numbers from 0 to 9
    for i in range(length):
        # Append each number at the end of list
        numberlist.append(1)
    return numberlist

def fragmentise(n):
    onesList = list_with_1s(n)
    numberlist = list(list_with_1s(n))
    
    permutations = [[list(numberlist)]]
    
    index = 0
    max = 2
    finished = False
    for i in range(n):
        for j in range(n):
            while not finished:
                if index < len(numberlist):
                    if numberlist[index]+1 <= max and len(numberlist)>2:
                        print("Length: ")
                        print(len(numberlist))
                        numberlist[index] = numberlist[index] + numberlist[-1]
                        numberlist.pop()
                        permutations.append(list(numberlist))
                        finished = True
                    else:
                        index += 1
                else:
                    finished = True
            finished = False
            
        finished = False
        numberlist = list(onesList)
        max += 1
        index = 0
    return permutations

permutations = fragmentise(8)
printer(permutations)















