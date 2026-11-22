class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = set(nums)
        longest = 0

        for num in new_nums:
            if num - 1 not in new_nums:
                length = 1
                checker = num
                while checker + 1 in new_nums:
                    checker += 1
                    length += 1
                longest = max(longest, length)

        return longest
            