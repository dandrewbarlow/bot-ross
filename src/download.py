'''
Andrew Barlow
Script to download a lot of Bob Ross Paintings and make them square
'''

import os
from os import error
import requests
from tqdm import tqdm

import numpy as np
from PIL import Image


url = "https://www.twoinchbrush.com/images/painting"

def downloadPaintings():
    # Go through all the paintings, use a status bar to avoid frustration
    for i in tqdm(range(1, 412), desc="Downloading paintings"):

        filename = './img/raw/' + str(i) + '.png'

        # if the file already exists, don't download it again
        if not os.path.isfile(filename):
            # Download picture, throw error and error name if it occurs
            try:
                picture = requests.get(url + str(i) + '.png').content
            except error:
                print( "Download Error:" + str(error) )

            # Save the picture
            file = open(filename, "wb")
            file.write( picture )
            file.close()
        else:
            print("File (" + filename + ") already exists")

# square images are required. since I want to preserve the full bob ross style, 
# I'm gonna fill the bottom rows w/ black and strip them again afterwards
def makeSquare():
    width = 450
    height = 113
    #matrix = np.zeros([height, width, 3], dtype=np.uint8)

    rawImgDir = "img/raw/"
    newImgDir = "img/formatted/"

    for filepath in tqdm( os.listdir(rawImgDir) ):
        try:
            img = Image.open(rawImgDir + filepath)
            imgArray = np.array(img)
            imgSize = (np.shape(imgArray))
            if np.shape(imgArray)[0] < 450:
                matrix = np.zeros( [450 - imgSize[0], imgSize[1], 3], dtype=np.uint8 )
                resultArray = np.append(imgArray, matrix, axis=0)
                result = Image.fromarray(resultArray)
                result.save(newImgDir + filepath)
        except:
            print("Error, skipping " + filepath)




def main():
    downloadPaintings()
    makeSquare()

main()