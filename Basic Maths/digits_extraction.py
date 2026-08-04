#  n = 7789 
# now extract the digits or count it 


n = 7789


def count_digit(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    if n == 0:
        digits.reverse()
    return digits


print(count_digit(n))