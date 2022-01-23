from collections import Counter
from operator import itemgetter
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return min(count.items(), key=itemgetter(1))[0]
# Or
from collections import Counter
from operator import itemgetter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans