class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = int(str(abs(x))[::-1])
        if x == abs(reversed_num):
            return True 
        else:
            return False