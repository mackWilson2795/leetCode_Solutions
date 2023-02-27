class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return nums
        i = 0
        i2 = 1
        val = nums[0]
        while i < len(nums):
            if nums[i] == val:
                i += 1
            else:
                nums[i2] = nums[i]
                val = nums[i2]
                i2 += 1
        return i2