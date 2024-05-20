import unittest
import findDominantColours

class TestDominantColours(unittest.TestCase):

    # an input pucture is racoon.png, with dominant colour white (background)
    def test_findDominantColours_pic(self):
        result = findDominantColours.findDominantColours('./samples/racoon.png')
        self.assertEqual(result, (255, 255, 255))
    
    # an input pucture is racoon.png, and returnTopN
    def test_findDominantColours_withPicAndTop(self):
        result = findDominantColours.findDominantColours('./samples/racoon.png', returnTopN = 5)
        self.assertEqual(result, [(255, 255, 255), (50, 50, 50), (120, 140, 120), (60, 70, 70), (90, 90, 80)])

    # an input pucture is racoon.png, and ignoreColour list
    def test_findDominantColours_withPicAndIgnore(self):
        result = findDominantColours.findDominantColours('./samples/racoon.png', ignoreColours = [(255, 255, 255), (50, 50, 50), (120, 140, 120)])
        self.assertEqual(result, (60, 70, 70))

    # an input pucture is racoon.png, returnTopN and ignoreColour list
    def test_findDominantColours_withPicAndTopAndIgnore(self):
        result = findDominantColours.findDominantColours('./samples/racoon.png', 2, [(255, 255, 255), (120, 140, 120), (60, 70, 70)])
        self.assertEqual(result, [(50, 50, 50), (90, 90, 80)])

    # check that function returns dominants
    def test_findNDominants(self):
        colourToFrequencyMap = {(11, 11, 11) : 22, (22, 22, 22) : 3, (33, 33, 33) : 7, (44, 44, 44) : 25, (55, 56, 55) : 9, (66, 66, 66) : 1}
        result = findDominantColours.findNDominants(colourToFrequencyMap, 5)
        self.assertEqual(result, [(44, 44, 44), (11, 11, 11), (55, 56, 55), (33, 33, 33), (22, 22, 22)])

    # return the dominant
    def test_findNDominant(self):
        colourToFrequencyMap = {(1, 1, 1) : 22, (2, 2, 2) : 3, (3, 3, 3) : 7, (4, 4, 4) : 25, (5, 6, 5) : 9, (6, 6, 6) : 1}
        result = findDominantColours.findNDominant(colourToFrequencyMap)
        self.assertEqual(result, (4, 4, 4))

if __name__ == '__main__':
    unittest.main()
