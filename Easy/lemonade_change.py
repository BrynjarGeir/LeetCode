class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0, 0, 0]
        for bill in bills:
            if bill == 5: change[0] += 5
            elif bill == 10: 
                change[1] += 10; change[0] -= 5
            else:
                change[2] += 20; 
                if change[1] >= 10:
                    change[1] -= 10; change[0] -= 5
                else:
                    change[0] -= 3*5
            if change[0] < 0 or change[1] < 0 or change[2] < 0: return False
        return True