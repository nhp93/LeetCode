class Solution:
    def clumsy(self, n: int) -> int:
        res = n
        i = n-1
        k = 0
        while i > 0:
            rem = k % 4
            if rem == 0:
                res *= i
            elif rem == 1:
                res = res // i
            elif rem == 2:
                res += i
            else:
                if i-2 > 0:
                    res -= i * (i-1) // (i-2)
                    i -= 2
                    k += 2
                else:
                    res -= i
            print(res)
            i -= 1
            k += 1
        return int(res)