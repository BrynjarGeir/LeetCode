class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        inGoing = [path[1] for path in paths]
        outGoing = [path[0] for path in paths]
        return [c for c in inGoing if c not in outGoing][0]
        