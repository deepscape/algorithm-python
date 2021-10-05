from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # print(nums[0] + nums[1])

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, i+1]


if __name__ == '__main__':
    s = Solution()
    result: List[int] = s.two_sum([2, 7, 11, 5], 9)
    print(result)