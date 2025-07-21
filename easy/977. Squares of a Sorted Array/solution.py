class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 2 pointers:
        l = len(nums)
        left = 0
        right = l-1
        
        result = []
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result.append(nums[left]**2)
                left +=1
            else:
                result.append(nums[right]**2)
                right -=1
        result.reverse()
        return result
