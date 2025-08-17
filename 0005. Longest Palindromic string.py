def expandCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(len(s)):
            odd = expandCenter(s, i, i)
            even = expandCenter(s, i, i + 1)
            max_length = max(odd, even)
            
            if max_length > (end - start):
                start = i - (max_length - 1) // 2
                end = i + max_length // 2

        return s[start:end + 1]
