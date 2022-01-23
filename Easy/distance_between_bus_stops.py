class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        oneway = 0; oranother = 0; start1 = start2 = start; n = len(distance) - 1
        while start1 != destination:
            oneway += distance[start1]
            if start1 == n: start1 = 0
            else: start1 += 1
        while start2 != destination:
            if start2 == 0:
                oranother += distance[-1]
                start2 = n
            else:
                oranother += distance[start2-1]
                start2 -= 1
        return oneway if oneway < oranother else oranother