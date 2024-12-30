class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        boolean_array = [True] * len(candies)
        for i in range(len(candies)):
            for j in range(len(candies)):
                if(candies[i]+extraCandies < candies[j]):
                    boolean_array[i] = False 
        return boolean_array