
class Solution:
    def longest_palindrome(self, string: str) -> str:
        # palindrome 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(string) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left + 1: right - 1]

        # 해당 사항 없을 때 빠르게 리턴
        if len(string) < 2 or s == s[::-1]:
            return string

        result = ''

        # Sliding Window 우측으로 이동
        for i in range(len(string) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.longest_palindrome("abba"))
