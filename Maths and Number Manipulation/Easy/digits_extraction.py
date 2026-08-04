class Solution :
    def extract_digit(self , n):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = n // 10
        digits.reverse()
        return digits


