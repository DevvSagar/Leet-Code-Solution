class Solution:
    def countDigit(self, n):
        digits = []
        while(n > 0):
            digits.append(n % 10)
            n = n // 10
        return len(digits)


