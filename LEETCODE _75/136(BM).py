class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            result ^= nums[i]

        return result

        '''x
        Approach:

        Using XOR with each number and getting last answer as single number.
        '''