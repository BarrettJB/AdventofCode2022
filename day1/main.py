def read_input():
    arr_input = []
    with open(FILE) as f:
        elf = []
        for line in f.readlines():
            if(line == '\n'):
                arr_input.append(elf)
                elf = []
            else:
                elf.append(int(line))
    #add last elf
    arr_input.append(elf)
    return arr_input

FILE = "input.txt"

if __name__ == "__main__":
    elves = read_input()
    max = 0
    for elf in elves:
        cals = 0
        for item in elf:
            cals = cals + item
        if(cals > max):
            max = cals
    
    print("-----------------------")
    print("          Part 1       ")
    print("Most calories: {}".format(max))
    print("-----------------------")

    bests = [0,0,0]
    for elf in elves:
        cals = 0
        for item in elf:
            cals = cals + item
        for idx, best in enumerate(bests):
            if(cals > best):
                bests.insert(idx, cals)
                bests.pop()
                break
    
    sum = 0
    for elf in bests:
        sum = sum + elf
    print("-----------------------")
    print("          Part 2       ")
    print("Top 3: {}".format(sum))
    print("-----------------------")