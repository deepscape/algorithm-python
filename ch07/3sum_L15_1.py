from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two point 간격을 좁혀가면서 합 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 < 0:
                    left += 1
                elif sum3 > 0:
                    right -= 1
                else:
                    # sum3 == 0 인 경우이므로 정답
                    results.append((nums[i], nums[left], nums[right]))
                    # 중복된 값 스킵처리
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results


if __name__ == '__main__':
    s = Solution()
    r: List = s.threeSum([-4, -1, -1, 0, 1, 2])
    print(r)
