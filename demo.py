import findDominantColours

filePath = './samples/racoon.png' # pathToYourImg.canBeDifferentExtensions
ignoreColours = [(255, 255, 255)]  # white
dominantColour = findDominantColours.findDominantColours(filePath, ignoreColours = ignoreColours)
top3Colours = findDominantColours.findDominantColours(filePath, returnTopN = 3)
print('The most dominant colour is: ' + str(dominantColour))
print('The top 3 dominant colours are: ' + str(top3Colours))