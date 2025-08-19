class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        output = 0
        left = 0

        for right in range(len(s)):
            if s[right] not in seen:
                output = max(output, right - left + 1 ) 
            else:
                if seen[s[right]] < left:
                    output = max(output, right - left + 1 ) 
                else:
                    left = seen[s[right]] + 1
                
            seen[s[right]] = right
        return output

