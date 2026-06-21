class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            n = sorted(str(abs(num)), reverse = True)
            res = ''.join(n)
            # res = '-' + res
            return int(res) * -1
        else:
            n = sorted(str(num))
            if n[0] == '0':
                for i in range (len(n)):
                    if n[i] > '0':
                        n[i], n[0] = n[0], n[i]
                        break
            res = ''.join(n)
        return int(res)

