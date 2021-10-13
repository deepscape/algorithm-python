from typing import List

# hash table 에서 O(1)로 단번에 조회하겠다는 전략
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_map= {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺸 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]


if __name__ == '__main__':
    s = Solution()
    result: List[int] = s.two_sum([7, 11, 2, 5], 9)
    print(result)