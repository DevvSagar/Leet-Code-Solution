
class Solution:
    def countDigit(self, n):
        digits = []
        while(n > 0):
            digits.append(n % 10)
            n = n // 10
        return len(digits)


# if you are solving on leet code u dont need the code written below !!!!!

solution = Solution()
answer = solution.countDigit(7789)
print(answer)