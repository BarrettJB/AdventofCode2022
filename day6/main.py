def readinput():
    with open(FILE) as f:
        return f.readlines()

FILE = 'input.txt'

if __name__ == "__main__":
    input = readinput()
    input = input[0]
    sequence = ['','','','']
    dupes = True
    seq_idx = 0
    sig_idx = 4

    sequence[0] = input[0]
    sequence[1] = input[1]
    sequence[2] = input[2]
    sequence[3] = input[3]

    while True:
        #check for dupes in the seq
        has_dupe = False
        for i in range(len(sequence)):
            for j in range(i+1,len(sequence)):
                if(sequence[i] == sequence[j]):
                    has_dupe = True
        
        if(not has_dupe):
            break

        sequence[seq_idx] = input[sig_idx]
        seq_idx = (seq_idx + 1) % 4
        sig_idx += 1

        

    p1 = sig_idx
    print("-----------------------")
    print("          Part 1       ")
    print("{}".format(p1))
    print("-----------------------")

    sequence = ['']*14
    dupes = True
    seq_idx = 0
    sig_idx = len(sequence)

    for i in range(len(sequence)):
        sequence[i] = input[i]

    while True:
        #check for dupes in the seq
        has_dupe = False
        for i in range(len(sequence)):
            for j in range(i+1,len(sequence)):
                if(sequence[i] == sequence[j]):
                    has_dupe = True
        
        if(not has_dupe):
            break

        sequence[seq_idx] = input[sig_idx]
        seq_idx = (seq_idx + 1) % len(sequence)
        sig_idx += 1

    p2 = sig_idx
    print("#######################")
    print("          Part 2       ")
    print("{}".format(p2))
    print("#######################")