class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []; most_candies = max(candies)
        for candie in candies:
            if candie + extraCandies >= most_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans