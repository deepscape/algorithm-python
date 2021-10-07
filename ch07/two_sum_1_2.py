from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement) + (i + 1)]


if __name__ == '__main__':
    s = Solution()
    result: List[int] = s.two_sum([7, 11, 2, 5], 9)
    print(result)