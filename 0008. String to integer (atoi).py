class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip() 
        if not int or s == "":
            return 0

        result = ""
        if s[0] == "-":
            result += "-"
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        for char in s:
            if char not in "0123456789":
                break
            result += char

        if result == "" or result == "-":
            return 0

        num = int(result)
        int_max = 2**31 - 1
        int_min = -2**31
        if num < int_min:
            return int_min
        if num > int_max:
            return int_max
        return num
