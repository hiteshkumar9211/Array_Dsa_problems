class Solution:
    def peakElement(self,arr,n):
      if(n==1):
          return 0
      if (arr[0]>=arr[1]):
           return 0
      if(arr[n-1]>=arr[n-2]):
            return n-1
      for i in range(n):
         if (arr[i]>=arr[i-1])and(arr[i]>=arr[i+1]):
            return i
