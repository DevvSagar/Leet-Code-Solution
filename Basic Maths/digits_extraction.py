#  n = 7789 
# now extract the digits or count it 



class Solution :
    def extract_digit(self , n):
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = n // 10
        digits.reverse()
        return digits


solution = Solution()
answer = solution.extract_digit(7789)
print(answer)