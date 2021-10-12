from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            print(stack)
            # [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
            while stack and height[i] > height[stack[-1]]:      # [-1] 은 마지막 요소값
                top = stack.pop()

                if not len(stack):
                    break

                # 이전의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters

            stack.append(i)

        return volume


if __name__ == '__main__':
    s = Solution()
    print(s.trap([4, 2, 0, 3, 2, 5]))
    #print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    #print(s.trap([2, 0, 0, 0, 0, 0]))
