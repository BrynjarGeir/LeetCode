class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        smallestTwo = [2**31-1]*2
        largestThree = [-2**31]*3
        for num in nums:
            if num <= smallestTwo[0]:
                smallestTwo[0] = num
                smallestTwo.sort(reverse=True)
            if num >= largestThree[0]:
                largestThree[0] = num
                largestThree.sort()
        return max(smallestTwo[0]*smallestTwo[1]*largestThree[2], 
                   largestThree[0]*largestThree[1]*largestThree[2])