from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        # s = s[::-1]
        print(s)


if __name__ == '__main__':
    s = Solution()
    s.reverseString(["h", "e", "l", "l", "o"])
