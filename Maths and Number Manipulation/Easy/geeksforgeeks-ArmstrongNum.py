class Solution:
    def armstrongNumber (self, n):
        duplicate_n = n
        sum = 0
        while(n > 0):
            digits = n % 10
            n = n // 10 
            sum += (digits ** 3)
        if sum == duplicate_n:
            return True
        else: 
            return False