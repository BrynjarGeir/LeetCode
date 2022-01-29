class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1]); units = 0
        while truckSize > 0 and boxTypes:
            curr = boxTypes.pop(-1)
            while curr[0] > 0 and truckSize > 0:
                units += curr[1]
                curr[0] -= 1
                truckSize -= 1
        return units