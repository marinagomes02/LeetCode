class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if (digits == ""):
            return []
        digits.replace("1", "")

        phone = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        stack = [(0,"")]
        combinations = []

        while stack:
            index, comb = stack.pop()
            if index == len(digits):
                combinations.append(comb)
            else:
                letters = phone[digits[index]]
                for letter in letters:
                    stack.append((index + 1, comb + letter))
        
        return combinations


# Test Cases
result = Solution()
assert(result.letterCombinations('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"])
assert(result.letterCombinations('2') == ["a","b","c"])