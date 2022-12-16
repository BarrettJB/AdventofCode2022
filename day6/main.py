def readinput():
    with open(FILE) as f:
        return f.readlines()

FILE = 'test.txt'

if __name__ == "__main__":
    input = readinput()
    input = input[0]
    sequence = ['','','','']
    seq_idx = 0
    sig_idx = 4

    sequence[0] = input[0]
    sequence[1] = input[1]
    sequence[2] = input[2]
    sequence[3] = input[3]

    while True:
        sig_char = input[sig_idx]
        for seq_char,idx in enumerate(sequence):
            if (seq_char == sig_char):
                break

        else:
            break
        sequence[seq_idx] = sig_char
        seq_idx = (seq_idx + 1) % 4
        sig_idx += 1
        

    p1 = sig_idx
    p2 = 0

    print("-----------------------")
    print("          Part 1       ")
    print("{}".format(p1))
    print("-----------------------")

    print("#######################")
    print("          Part 2       ")
    print("{}".format(p2))
    print("#######################")