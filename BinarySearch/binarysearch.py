def binary_search(arr,key):
    n=len(arr)
    start=0
    end = n-1
    while(start<=end):
        mid=start+(end-start)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]>key):
            end=mid-1
        else:
            start=mid+1
    return -1 

 print(binary_search([10,20,30,40,50,60],10)
