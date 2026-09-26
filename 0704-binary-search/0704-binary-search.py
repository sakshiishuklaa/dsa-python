class Solution:
    def search(self, nums: list[int], target: int) -> int:
        end=len(nums)-1
        start=0
        while(start<=end):
            mid=start+(end-start)//2
            if target==nums[mid]:
                return mid
                break
            elif target>nums[mid]:
                start=mid+1
                
            else:
                end=mid-1
            
        return -1        
