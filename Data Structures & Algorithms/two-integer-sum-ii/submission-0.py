class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1

        while i < j:
            nsum = numbers[i] + numbers[j]
            if nsum == target:
                return [i+1, j+1]
            elif nsum < target:
                i+=1
            else:
                j-=1
        