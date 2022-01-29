class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        even = ['a', 'c', 'e', 'g']
        if (coordinates[0] in even and int(coordinates[1]) %2 == 0) or (coordinates[0] not in even and int(coordinates[1]) % 2 != 0):
            return True
        else: return False