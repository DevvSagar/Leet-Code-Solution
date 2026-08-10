import math 
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        digits = 0
        square_root = math.sqrt(num)
        print(square_root)
        for i in range(1 , square_root):
            if num % i == 0:
                digits += i 
        if digits == num:
            return True
        return False
