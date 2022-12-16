def readinput():
    with open(FILE) as f:
        return f.readlines()

class Task:
    low = -1
    hi = -1

    #takes in a string like the input
    #eg 2-54
    def __init__ (self, str):
        nums = str.split('-')
        self.low = int(nums[0])
        self.hi = int(nums[1])
    
    def full_overlaps(self, other):
        if ((self.low >= other.low) and (self.hi <= other.hi)):
            return True
        elif ((self.low <= other.low) and (self.hi >= other.hi)):
            return True
        else:
            return False
    
    def partial_overlap(self, other):
        if((self.low <= other.low) and (self.hi >= other.low)):
            return True
        elif((self.low <= other.hi) and (self.hi >= other.hi)):
            return True
        elif((self.low >= other.low) and (self.hi <= other.hi)):
            return True
        else:
            return False


FILE = 'input.txt'

if __name__ == "__main__":
    input = readinput()
    p1 = 0
    p2 = 0
    for line in input:
        task_desc = line.split(',')
        task1 = Task(task_desc[0])
        task2 = Task(task_desc[1])
        p1 += task1.full_overlaps(task2)
        p2 += task1.partial_overlap(task2)

    print("-----------------------")
    print("          Part 1       ")
    print("{}".format(p1))
    print("-----------------------")

    print("#######################")
    print("          Part 2       ")
    print("{}".format(p2))
    print("#######################")