
#print ("input 3 integers you want to see in order")

#x = int(input())
#y = int(input())
#z = int(input())
#yes = [x, y, z]

def RyanBubbleSort1(yes):
    n = len(yes)


    for i in range(n):


        for j in range(0, n-i-1):

            if yes[j] > yes[j+1] :
                yes[j], yes[j+1] = yes[j+1], yes[j]
    return yes
#RyanBubbleSort1(yes)

#print ("The array in numerical order is:")
#for i in range(len(yes)):
#print ("%d" %yes[i]),