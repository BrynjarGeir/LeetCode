class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        size = len(arr); goods = 0
        for i in range(size - 2):
            for j in range(i+1, size -1):
                for k in range(j+1, size):
                    good_a = abs(arr[i] - arr[j]) <= a
                    good_b = abs(arr[j] - arr[k]) <= b
                    good_c = abs(arr[i] - arr[k]) <= c
                    
                    if all((good_a, good_b, good_c)):
                        goods += 1
        return goods
                    