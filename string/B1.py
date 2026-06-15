def sort_a(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j]<arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
def print_sort(arr):
    sort_a(arr)      
    print(arr)          
                
a=[1,2,3,1,21,24,34,2,12,10,9]
print_sort(a)             