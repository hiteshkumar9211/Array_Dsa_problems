def reverse(start,end,arr):
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
def rotate_right(arr,d):
    N = len(arr)
    reverse(0,N-1,arr)
    reverse(0,d-1,arr)
    reverse(d,N-1,arr)
    return arr
def rotate_left(arr,d):
    N = len(arr)
    reverse(0,d-1,arr)
    reverse(d,N-1,arr)
    reverse(0,N-1,arr)
    return arr
def main():
    arr1 = [1,2,3,4,5,6]
    print(arr1)
    arr1 = rotate_right(arr1,2)
    print(arr1)
    arr2 = [1,2,3,4,5,6]
    arr2 = rotate_left(arr2,2)
    print(arr2)
if __name__ == '__main__':
    main()
    
    