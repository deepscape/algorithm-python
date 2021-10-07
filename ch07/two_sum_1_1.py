from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    s = Solution()
    result: List[int] = s.two_sum([7, 11, 2, 5], 9)
    print(result)