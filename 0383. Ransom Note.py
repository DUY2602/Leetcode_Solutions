class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        can_be_constructed = True
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i, "", 1)
            else:
                can_be_constructed = False
        
        return can_be_constructed
