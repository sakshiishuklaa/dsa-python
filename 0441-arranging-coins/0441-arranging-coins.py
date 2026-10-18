class Solution:
    def arrangeCoins(self, n: int) -> int:
        start=1
        end=n
        result=0
        while start<=end:
            mid=start+(end-start)//2
            coins=(mid*(mid+1))//2
           
            if coins == n:
                return mid
            elif coins < n :
                start=mid+1
                result=mid
            else:
                end=mid-1
        return result 

