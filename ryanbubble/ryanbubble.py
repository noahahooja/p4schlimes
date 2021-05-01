print ("input three integers")

x = int(input())
y = int(input())
z = int(input())
arr = [x, y, z]

def RyanBubble(arr):
    n = len(arr)


    for h in range(n):


        for p in range(0, n-h-1):

            if arr[p] > arr[p+1] :
                arr[p], arr[p+1] = arr[p+1], arr[p]

RyanBubble(arr)

print ("Array = :")
for h in range(len(arr)):
    print ("%d" %arr[h]),