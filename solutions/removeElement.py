class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i, v in enumerate(nums):
            if v == val:
                count += 1
            elif count > 0:
                nums[i-count] = v
        return len(nums) - count