class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.combine_sum_2(candidates, 0, [], ans, target)
        print(ans)
        return ans
    
    def combine_sum_2(self, candidates, start, path, ans, target):
        if not target:
            ans.append(path)
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]: continue
            if candidates[i] > target: break
                
            self.combine_sum_2(candidates, i + 1, path + [candidates[i]], ans, target - candidates[i])