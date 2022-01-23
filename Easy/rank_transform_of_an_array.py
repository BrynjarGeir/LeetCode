class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sor = sorted(list(set(arr))); rank = 1; ranks = {}
        for s in sor:
            if s not in ranks:
                ranks[s] = rank
                rank += 1
        ans = []
        for a in arr:
            ans.append(ranks[a])
        return ans
        