class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        # 2 pointers 
        right = l-1
        left = 0

        while numbers[right]+numbers[left] != target:
            curr = numbers[right]+numbers[left]
            if curr> target:
                right-=1
            else:
                left+=1
        
        return[1+left, 1+right]
        
