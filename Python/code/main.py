# User function Template for python3

def rotate(arr, n):
    last = arr[-1]

    while n > 1:
        arr[n-1] = arr[n-2]
        n -= 1
    arr[0] = last


def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends