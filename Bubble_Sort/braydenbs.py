
  
def BraydenBubbleSort(arr):
    n = len(arr)
  

    for i in range(n):
  

        for j in range(0, n-i-1):
  
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  

arr = [32, 49, 328, 92, 23, 8, 29]
  
BraydenBubbleSort(arr)
  
print ("The array in numerical order is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 