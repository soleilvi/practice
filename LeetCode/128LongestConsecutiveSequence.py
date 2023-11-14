class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = [(0, 0)]  # Place edge numbers in tuples, then return the greatest difference between the two numbers
        i = 0

        if len(s) == 1:
            return 1

        for num in s:
            if num + 1 in s and not num - 1 in s:
                l[i][0] = num
                i += 1
            elif num - 2 in s and not num + 1 in s:
                l[i][1] = num
                i += 1
                
        