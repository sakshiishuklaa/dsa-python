class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count={}
        maximum=0
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
            else:
                count[nums[i]]+=1
        for key in count:
            if maximum<count[key]:
                maximum=count[key]
                sol=key
        return sol