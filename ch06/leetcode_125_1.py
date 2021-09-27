class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # Palindrome
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("race a car"))
