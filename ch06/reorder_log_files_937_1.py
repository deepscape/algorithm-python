from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 식별자를 제외한 문자열 [1:] 을 키로 정렬하며, 동일한 경우 후순위로 식별자 [0]을 지정해 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        print(letters + digits)

        return letters + digits


if __name__ == '__main__':
    s = Solution()
    s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])

