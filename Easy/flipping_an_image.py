import numpy as np
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image = np.array(image)
        image = np.flip(image, axis = 1)
        image = 1 - image
        return image