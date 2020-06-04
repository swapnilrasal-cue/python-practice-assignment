def binary_search(arr, first, last, x):
    if last >= first: 
        mid = (last + first) // 2
    
        if arr[mid] == x: 
            return mid 
  
        elif arr[mid] > x: 
            return binary_search(arr, first, mid - 1, x) 
  
        else: 
            return binary_search(arr, mid + 1, last, x) 
  
    else: 
        return -1

def search(arr , key):
    for element in arr:
        if element == key:
            return True
    return False
            
        
    
a = [2,5,7,8,44]
key = int(input("enter key you want to search : "))

print(search(a,key))

if __name__=="__main__":
    result = binary_search(a,0,len(a)-1,key)
    
    if result != -1:
        print("Element Found")
    else:
        print("Element Not Found")
    
