class Solution:
    def reorderSpaces(self, text: str) -> str:
        wo = text.split()
        if len(wo) == 1: return wo[0] + ' '*text.count(' ')
        sp = text.count(' ')
        be = sp//(len(wo)-1)
        af = sp - (sp//(len(wo)-1))*(len(wo)-1)
        ans = ' '*be
        ans = ans.join(wo) + ' '*af
        return ans