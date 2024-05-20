from PIL import Image
import heapq
import operator

# input is a path to a file, returnTopN - request to return N top most popular colours, ignoreColours - list of tuples of RGB we should ignore
# if returnTopN - None, functon returns the most popular coour. If ignoreColours is not empty we won't keep in mind colours from the list
# output the RGB value/s of the most frequent (dominant) colour/s in the image
def findDominantColours(filePath, returnTopN = None, ignoreColours = []):
    img = Image.open(filePath)
    rgbImg = img.convert('RGB') 
    
    # if there are colours in ignoreColours list, we are going to round it, to be able to match our pixels' values
    listToIgnoreReducedColours = [reduceColourSpace(colour) for colour in ignoreColours]

    colourToFrequencyMap = fillColourToFrequencyMap(rgbImg, listToIgnoreReducedColours)

    if returnTopN == None:
        print(findNDominant(colourToFrequencyMap)) # delete
        return findNDominant(colourToFrequencyMap)
    else:
        listOfNDominantColours = findNDominants(colourToFrequencyMap, returnTopN)
        print(listOfNDominantColours) # delete
        return listOfNDominantColours

# going through each pixel and collecting colours in the map and counting how many times we have met the colour
# input: converted to RGB format pircture, list of colours we should to ignore, map to fill in
def fillColourToFrequencyMap(rgbImg, listToIgnoreReducedColours):
    imgWidth, imgHight = rgbImg.size
    colourToFrequencyMap = {}
    
    # going through 2D array, where x is length of an array and y length of an inner array
    for x in range(imgWidth):
        for y in range(imgHight):
            red, green, blue = rgbImg.getpixel((x, y)) # returns RGB values
            tupleRoundedRGB = reduceColourSpace((red, green, blue))

            # if tupleRoundedRGB in list of colours we gave to ignore, we have to skip this value
            if len(listToIgnoreReducedColours) > 0 and tupleRoundedRGB in listToIgnoreReducedColours:
                continue

            addColourAndIncreasefrequency(tupleRoundedRGB, colourToFrequencyMap)
    return colourToFrequencyMap

# round the RGB values of a pixel to the math nearest multiple of 10, to avoid very minor colour differences impacting the results
# input: tuple with original RGB, output: tuple with rounded RGB
def reduceColourSpace(tupleOriginRGB):
    tupleRoundedRGB = ()
    for colour in tupleOriginRGB:
        roundedColour = round(colour / 10) * 10 if colour < 255 else colour
        tupleRoundedRGB += (roundedColour,)
    return tupleRoundedRGB

# checks if tuple already in map, if it is increase counter else add tuple as a key and set counter to 1
# input: tuple with rounded RGB and map with frequency of tuple
def addColourAndIncreasefrequency(tupleRoundedRGB, colourToFrequencyMap):
    newFrequency = colourToFrequencyMap.get(tupleRoundedRGB, 0) + 1
    colourToFrequencyMap[tupleRoundedRGB] = newFrequency

# We need to go one more time over the map to find the most popular colour
# input: the map with colours and frequency. 
# output: RGB of the most popular colour
def findNDominant(colourToFrequencyMap):
    return max(colourToFrequencyMap.items(), key=operator.itemgetter(1))[0]

# if returnTopN provided, we need create a lst with top N popular colours
# input: map with colours and frequency and how many colours we need to return
# output: list of top popular colours by counter
def findNDominants(colourToFrequencyMap, returnTopN):
    heapOfcolours = buildMaxPriorityQueue(colourToFrequencyMap)
    listOfTopNcolours = []
    for i in range(returnTopN):
        listOfTopNcolours.append(heapq.heappop(heapOfcolours)[1])
    return listOfTopNcolours

# building max priority queue and returns it
def buildMaxPriorityQueue(colourToFrequencyMap):
    # priority queue works as min-heap. So we will reverse our heap by multiplng our counter to -1
    tuplelist = list((-value, key) for key, value in colourToFrequencyMap.items())
    heapq.heapify(tuplelist)
    return tuplelist

# To run the main process you can uncomment the code bellow
filePath = './samples/racoon.png' # pathToYourImg.canBeDifferentExtensions
ignoreColours = [(255, 255, 255)]  # white
dominantColour = findDominantColours(filePath, ignoreColours = ignoreColours)
top3Colours = findDominantColours(filePath, returnTopN = 3)
print('The most dominant colour is: ' + str(dominantColour))
print('The top 3 dominant colours are: ' + str(top3Colours))