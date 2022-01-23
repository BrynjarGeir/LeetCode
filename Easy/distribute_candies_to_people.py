class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ind = 0; current = 1; ans = [0]*num_people
        while candies > 0:
            if candies > current:
                ans[ind] += current
                candies -= current
            else:
                ans[ind] += candies
                candies = 0
            if ind == len(ans)-1: ind = 0
            else: ind += 1
            current += 1
        return ans