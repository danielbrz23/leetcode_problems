class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 2 pointers:
        l = len(s)
        left = 0
        right = l-1

        while right>left:
            curr = s[left]
            s[left] = s[right]
            s[right] = curr

            left+=1
            right-=1
