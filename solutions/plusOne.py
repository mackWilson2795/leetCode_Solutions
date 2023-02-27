class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        idx = -1
        l = len(digits)
        while remainder:
            if abs(idx) == l:
                if digits[idx] < 9:
                    digits[idx] += 1
                else:
                    digits.insert(0, 1)
                    digits[idx] = 0
                remainder = 0
            elif digits[idx] < 9:
                digits[idx] += 1
                remainder = 0
            else:
                digits[idx] = 0
            idx -= 1
        return digits