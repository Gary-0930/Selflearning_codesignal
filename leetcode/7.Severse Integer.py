class Solution:
    def reverse(self, x: int) -> int:
        if x > 2 ** 31:
            return 0
        elif x >= 0:
            length = len(str(x))
            n = length - 1
            A = 0
            while(n >= 0):
                y = x % 10 
                x = x // 10 
                A = y * 10 ** n + A
                n -= 1
            if A > 2 ** 31:
                return 0
            else:
                return A
        else:
            x = x * (-1)
            length = len(str(x))
            n = length - 1
            A = 0
            while(n >= 0):
                y = x % 10
                x = x // 10 
                A = y * 10 ** n + A
                n -= 1
            if A > 2 ** 31:
                return 0
            else:
                return A * (-1)
