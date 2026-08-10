class Solution:
    def isPrime(self, n):
        counter = 0
        i = 1
        while(i * i <= n):
            if n % i == 0:
                counter+=1
                if i != (n // i):
                    counter+=1
            i+=1
        if counter == 2:
            return True
        return False