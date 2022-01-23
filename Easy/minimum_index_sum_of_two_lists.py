class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {restaurant: i for i, restaurant in enumerate(list1)}
        dic2 = {restaurant: dic1[restaurant]+i for i, restaurant in enumerate(list2) if restaurant in dic1}
        
        MIN = 2**31-1
        ans = []
        
        for key, val in dic2.items():
            if val < MIN:
                ans = [key]
                MIN = val
            elif val == MIN:
                ans.append(key)
        return ans