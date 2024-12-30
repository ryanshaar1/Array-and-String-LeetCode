class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        smallest = float('inf')
        second_smallest = float('inf')

        for num in nums:
            if num <= smallest:
                smallest = num  
            elif num <= second_smallest:
                second_smallest = num 
            else:
                
                return True
        
        return False
