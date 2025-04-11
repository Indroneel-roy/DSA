from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0    

            else:
                digits.append(1)
                one = 0
            i += 1    
        return digits[::-1]            
if __name__ == "__main__":
    digits = [1,2,3]
    s = Solution()
    result = s.plusOne(digits)
    print(result)
        