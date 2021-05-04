print ("Input 5 Numbers that you want to sort")

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
arr = [a, b, c, d, e]

def CQBubbleSort(arr):
    n = len(arr)


    for i in range(n):


        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

CQBubbleSort(arr)

print ("The array in numerical order is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),