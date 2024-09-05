def isPalindrome(arr,start,end):
    if start >= end:
        return True
    if arr[start] == arr[end]:
        return isPalindrome(arr,start+1,end-1)
    else:
        return False
def isPalin_iter(arr):
    start = 0
    end = len(arr)
    for i in range(end//2):
        if arr[i] != arr[end-i-1]:
            return False
            break
    return True
def main():
   arr1 = [ 3, 6, 0, 6, 3 ]
   ans = isPalindrome(arr1,0,len(arr1)-1)
   print(ans)
   ans1 = isPalin_iter(arr1)
   print(ans1)
   arr2 = [1,2,0,1]
   ans = isPalindrome(arr2,0,len(arr2)-1)
   print(ans)
   ans1 = isPalin_iter(arr2)
   print(ans1)
if __name__ =='__main__':
    main()

   