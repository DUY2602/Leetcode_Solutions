class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        test = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(test):
                test = test[:-1]
        
        return test
