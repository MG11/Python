# Recursively print all sentences that can be formed from list of word lists

R = 2
C = 2


def printfn(r, c, arr, output):
    if r >= R or c >= C:
        return
    output[r] = arr[r][c]

    if r == R - 1:
        for j in output:
            print(j, end=" ")
        print("\n")

    for j in range(C):
            printfn(r+1, j, arr, output)


def print_sentance():

    arr = [["you", " "],
           ["have", "are"]]
    output = [""]*R

    for i in range(C):
        if arr[0][i] != " ":
            printfn(0, i, arr, output)



if __name__ == "__main__":
    print_sentance()