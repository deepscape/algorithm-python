import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # empty list 로 값을 초기화하는 defaultdict 사용
        anagrams = collections.defaultdict(list)

        for word in strs:
            # eat tea ate 는 정렬하면 'aet' 로 같은 값이 됨
            # 'aet' 로 키를 같게 만든 상태에서, eat tea ate 를 값으로 추가
            anagrams[''.join(sorted(word))].append(word)

        print(anagrams)
        print(anagrams.values())
        # defaultdict( <class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})

        return anagrams.values()


if __name__ == '__main__':
    s = Solution()
    s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
