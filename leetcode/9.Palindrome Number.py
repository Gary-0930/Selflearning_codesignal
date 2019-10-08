class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            x = str(x)
            x_back = x[::-1]
            if x == x_back:
                return True
            else:
                return False
        else:
            return False
