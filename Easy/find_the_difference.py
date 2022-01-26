class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sList = list(s); tList = list(t)
        while sList:
            if sList[0] in tList:
                tIndex = tList.index(sList[0])
                tList.pop(tIndex)
                sList.pop(0)
            else:
                return sList[0]
        return tList[0]
# Or better
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)