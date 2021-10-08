from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:  # or 1개의 값을 제외한 나머지가 모두 0 이거나
            return 0

        volume = 0      # 빗물 총량
        left, right = 0, len(height) - 1        # 투 포인터 이동
        left_max, right_max = height[left], height[right]

        while left < right:
            # 포인터 이동할 때마다, 각 포인터가 가리키는 최대값을 갱신
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            # 더 높은 쪽을 향해 투 포인터 이동
            # 중요 : 오른쪽 최대값이 크다면 왼쪽 포인터가 이동하고, 왼쪽 최대값이 크다면 오른쪽 포인터가 이동한다.
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


if __name__ == '__main__':
    s = Solution()
    print(s.trap([4, 2, 0, 3, 2, 5]))
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([2, 0, 0, 0, 0, 0]))
