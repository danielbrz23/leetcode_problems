class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            y = str(x)
            l = len(y)
            if l == 1:
                return True
            for i in range(l//2 +1):
                if y[i] != y[l-1-i]:
                    return False
            return True
        return False
