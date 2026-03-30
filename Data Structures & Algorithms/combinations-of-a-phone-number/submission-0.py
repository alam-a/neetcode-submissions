class Solution:
    def __init__(self):
        self.cm = {
            "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], 
            "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], 
            "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        result = []
        words = self.letterCombinations(digits[1:])
        words = words if words else [""]
        for char in self.cm[digits[0]]:
            for word in words:
                result.append(char+word)
        return result
        # for i in range(len(digits)):
        #     words = self.letterCombinations(digits[i+1:])
        #     for char in self.cm[digits[i]]:
        #         for word in words:
        #             result.append(char+word)
        # return result
            



        