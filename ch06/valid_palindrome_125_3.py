import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome("abba"))
