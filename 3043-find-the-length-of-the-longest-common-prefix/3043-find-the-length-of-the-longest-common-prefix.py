class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for a1 in arr1:
            num = str(a1)
            prefix = ""
            for c in num:
                prefix += c
                prefixes.add(prefix)
        
        lcp = 0
        for a2 in arr2:
            num = str(a2)
            prefix = ""
            for i, c in enumerate(num):
                prefix += c
                if prefix in prefixes:
                    lcp = max(lcp, i + 1)
                else:
                    break

        return lcp
        