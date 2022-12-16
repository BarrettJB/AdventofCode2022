"""
a:x:1
b:y:2
c:z:3

a<b<c
"""

def readinput():
    with open(FILE) as f:
        return f.readlines()

FILE = 'input.txt'

if __name__ == "__main__":
    input = readinput()
    p1 = 0
    for game in input:
        opp = game[0]
        you = game[2]
        if(you == "X"):
            p1 = p1 + 1
            if(opp == "A"):
                p1 = p1 + 3
            elif(opp == "C"):
                p1 = p1 + 6
        elif(you == "Y"):
            p1 = p1 + 2
            if(opp == "B"):
                p1 = p1 + 3
            elif(opp == "A"):
                p1 = p1 + 6
        elif(you == "Z"):
            p1 = p1 + 3
            if(opp == "C"):
                p1 = p1 + 3
            elif(opp == "B"):
                p1 = p1 + 6

    print("-----------------------")
    print("          Part 1       ")
    print("{}".format(p1))
    print("-----------------------")

    scores = {
        "A" : 1,
        "B" : 2,
        "C" : 3
    }

    results = {
        "X" : 0,
        "Y" : 3,
        "Z" : 6
    }

    p2 = 0
    for game in input:
        opp = game[0]
        you = game[2]
        if(you == "X"):
            move = ((scores[opp] - 2) % 3) + 1
            p2 = p2 + move + 0
        elif(you == "Y"):
            move = scores[opp]
            p2 = p2 + move + 3
        elif(you == "Z"):
            move = ((scores[opp]) % 3) + 1
            p2 = p2 + move + 6
             

    print("#######################")
    print("          Part 2       ")
    print("{}".format(p2))
    print("#######################")