def readinput():
    with open(FILE) as f:
        return f.readlines()

FILE = 'input.txt'

if __name__ == "__main__":
    input = readinput()
    print("-----------------------")
    print("          Part 1       ")
    print("{}".format(p1))
    print("-----------------------")

    print("#######################")
    print("          Part 2       ")
    print("{}".format(p2))
    print("#######################")