#User function Template for python3
class Solution:
    def reverse(self,arr,start,end):
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
    def rotate(self,arr):
        n = len(arr)
        d = 1
        self.reverse(arr,0,n-1)
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        return arr

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        t -= 1

# } Driver Code Ends
