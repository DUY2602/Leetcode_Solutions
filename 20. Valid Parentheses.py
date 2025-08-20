class Solution:
    def isValid(self, s: str) -> bool:
        pair = []
        mapping = {'(' : ')', '{' : '}', '[' : ']'}
        for paren in s:
            if paren in mapping.keys():
                pair.append(paren)
            else:
                if not pair or mapping[pair.pop()] != paren:
                    return False

        return not pair
        
