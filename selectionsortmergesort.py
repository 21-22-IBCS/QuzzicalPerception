import random
import time

def mergeSort(li2):
    if len(li2) > 1:
        m = len(li2)//2
        left = li2[:m]
        right = li2[m:]
        mergeSort(left)
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                li2[k] = left[i]
                i += 1
            else:
                li2[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            li2[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            li2[k] = right[j]
            j += 1
            k += 1
            
def selectionSort1(li):
    sortedList = []
    while len(li) > 0:
        minE = li[0]
        for i in range(len(li)):
            if li[i] < minE:
                minE = li[i]
        li.remove(minE)
        sortedList.append(minE)

    return sortedList

def selectionSort2(x):
    Min=0
    num=0

    for i in range(len(x)):
        Min=x[i]
        for j in range (i,len(x)):
            if (x[j]<Min):
                Min= x[j]
                num=j

        if (Min != x[i]):
            x[num]=x[i]
            x[i]=Min

    return x

def main():

    l1=[]
    l2=[]
    l3=[100,2000,300,400,500,1000,10000]
    n=100
    dSelection =[]
    dMerge = []

    for i in range(len(l3)):
        for j in range(l3[i]):
            l1.append(random.randint(1,n))
            l2.append(random.randint(1,n))

        start= time.time()
        selectionSort1(l1)
        stop = time.time()
        a= stop-start
        a=round(a,5)
        dSelection.append(a)

        start= time.time()
        mergeSort(l2)
        stop = time.time()
        b= stop-start
        b=round(b,5)
        dMerge.append(b)

        totalTime=0
    for t in dSelection:
        totalTime = totalTime + t

    print ("____________________________________________________________________")
    print ("Length of list\t"+"Time took for selection sort\t"+"Time took for merge sort")
    print ("____________________________________________________________________")
    for i in range (len(l3)):
        print (str(l3[i])+"\t\t\t"+str(dSelection[i])+"\t\t\t"+str(dMerge[i]))
        print ("____________________________________________________________________")

    
    

if __name__ == "__main__":
    main()
