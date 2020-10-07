'''
Andrew Barlow
Script to download a lot of Bob Ross Paintings
'''

import requests
from tqdm import tqdm

# from bs4 import BeautifulSoup as soup

url = "https://www.twoinchbrush.com/all-paintings/images/painting"

def main():

    for i in tqdm(range(1, 412)):
        picture = requests.get(url + str(i) + '.png').content
        file = open("img/" + str(i) + '.png', "wb")
        file.write( picture )
        file.close()

main()