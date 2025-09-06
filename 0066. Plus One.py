class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string_digits = ""
        for digit in digits:
            string_digits += str(digit)

        result = int(string_digits) + 1

        return list(map(int, str(result)))
