def readinput():
    with open(FILE) as f:
        return f.readlines()

FILE = 'input.txt'

if __name__ == "__main__":
    input = readinput()
    p1 = 0
    for _, line in enumerate(input):
        res = ''
        for i in range(0,len(line)//2):
            for j in range(len(line)//2,len(line)):
                char1 = line[i]
                char2 = line[j]
                if(char1 == char2):
                  res = char1
                  break
            else:
                continue
            break
        
        if(res.isupper()):
            p1 = p1 + ord(res)-64 + 26
        else:
            p1 = p1 + ord(res)-96


    print("-----------------------")
    print("          Part 1       ")
    print("{}".format(p1))
    print("-----------------------")

    p2 = 0
    i = 0
    while(i < len(input)):
        set1 = input[i][:-1]
        set2 = input[i+1][:-1]
        set3 = input[i+2][:-1]
        opts = ''
        res = ''
        for char1 in set1:
            for char2 in set2:
                if(char1 == char2):
                    opts += char1

        for char3 in set3:
            for char12 in opts:
                if(char3 == char12):
                    res = char3
                    break
            else:
                continue
            break

        if(res.isupper()):
            p2 += ord(res)-64 + 26
        else:
            p2 += ord(res)-96
        
        i+= 3

    print("#######################")
    print("          Part 2       ")
    print("{}".format(p2))
    print("#######################")