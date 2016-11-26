list = [9,8,7,6,5,4,3,2,1,0]
list1 = [9,8,7,6,5,4,3,2,1,0]
list2 = [9,8,7,6,5,4,3,2,1,0]
list3 = [9,8,7,6,5,4,3,2,1,0]
list4 = [9,8,7,6,5,4,3,2,1,0]

def swap(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
    return list
    
def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                swap(list, j,j+1)
    return list


def selectionsort(list):
    for i in range (len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[i]:
                min = j
                
        swap(list , min , i)
              
    return list


def mergesort(list):
    if len(list)<2:
        return list
    else:
        mid = len(list) / 2
        left_list = mergesort(list[:mid])
        right_list = mergesort(list[mid:])
        return merge(left_list, right_list)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result






def quicksort(x):
    if len(x) < 2 :
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

    
 
def insertionsort(list2):
    for i in range(1,len(list2)):
        #print i
        key = list2[i]
        j = i-1
        while j>=0 and list2[j]>key:
            list2[j+1] = list2[j]
            j = j - 1
        list2[j+1] = key
    return list2
            
    
#print "Bubble sort"
#print list
#print  bubblesort(list)

#print "Selection sort"
#print list1
#print selectionsort(list1)


#print "Merge sort"
#print list
#print mergesort(list)

#print "insertion sort"
#print list2
#print insertionsort(list2)

print "Quick sort"
print list3
print quicksort(list3)
