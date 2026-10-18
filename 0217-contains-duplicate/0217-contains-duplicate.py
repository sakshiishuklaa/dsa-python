class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dupli = {}

        for i in range(len(nums)):
            if nums[i] in dupli:
                return True
            else:
                dupli[nums[i]] = True

        return False