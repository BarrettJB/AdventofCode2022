def readinput():
    with open(FILE) as f:
        return f.readlines()

class BoxStack:
    boxes = []
    
    def __init__(self, lst):
       self.boxes = lst
    
    def MoveBoxes(self, count, dst):
        for _ in range(count):
            dst.AddBox(self.boxes.pop())

    def MoveBoxes9001(self, count, dst):
        dst.AddBox9001(self.boxes[-count:])
        del self.boxes[-count:]

    def AddBox(self, box):
        self.boxes.append(box)

    def AddBox9001(self, box):
        self.boxes += box

FILE = 'input.txt'

if __name__ == "__main__":
    input = readinput()
    numStacks = len(input[0])//4
    setup_idx = -1
    for idx,line in enumerate(input):
        if(len(line) == 1):
            #end of initial state found
            setup_idx = idx-2 #ignore stack numbers
            break
    
    if(setup_idx == -1):
        print("ERROR: Failed to find setup line")
        exit(-1)
    
    stacks = []
    for i in range(numStacks):
        boxes = []
        stack_idx = setup_idx
        while True:
            box = input[stack_idx][i*4+1]
            if box == " ":
                break
            boxes.append(box)
            stack_idx -= 1
            if(stack_idx < 0):
                break
        stacks.append(BoxStack(boxes))

    # for _, line in enumerate(input[setup_idx+3:]):
    #     move = line.split()
    #     stacks[int(move[3])-1].MoveBoxes(int(move[1]),stacks[int(move[5])-1])

    p1 = ""    
    # for stack in stacks:
    #     p1 += stack.boxes.pop()

    p2 = ""
    for _, line in enumerate(input[setup_idx+3:]):
        move = line.split()
        stacks[int(move[3])-1].MoveBoxes9001(int(move[1]),stacks[int(move[5])-1])

    for stack in stacks:
        p2 += stack.boxes.pop()

    print("-----------------------")
    print("          Part 1       ")
    print("{}".format(p1))
    print("-----------------------")

    print("#######################")
    print("          Part 2       ")
    print("{}".format(p2))
    print("#######################")