#import requests
#import csv
#from bs4 import BeautifulSoup
import json
import urllib.error
import urllib.parse
import urllib.request
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import urllib.request, json
import re
import subprocess

re.M



url_rtx3060ti = "https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203060%20Ti&manufacturer=NVIDIA"
url_rtx3070 = "https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203070&manufacturer=NVIDIA"
url_rtx3070ti = "https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203070%20Ti&manufacturer=NVIDIA"
url_rtx3080 = "https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203080&manufacturer=NVIDIA"
url_rtx3080ti = "https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203080%20Ti&manufacturer=NVIDIA"
url_rtx3090 = "https://api.nvidia.partners/edge/product/search?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203090&manufacturer=NVIDIA"


def getLinkRTX3000(site):
    # WEBDRIVER_PATH = os.path.abspath("C://Users/Jonas/Documents/Python Projekte/Nvidia-Notify-master/geckodriver.exe")
    # options = Options()
    # options.headless = True
    # driver = webdriver.Firefox(options=options, executable_path=WEBDRIVER_PATH)
    #
    # driver.get(site)
    #
    # #text = json.loads(driver.find_element_by_tag_name('body').text)
    # text = driver.find_element_by_tag_name('body').text
    #
    # driver.quit()

    with open(r"C:\Users\Jonas\Documents\Python Projekte\selenium\postscrape\karte.txt", "w") as f1:
        f1.write(site)

    subprocess.call([r'C:\Users\Jonas\Documents\Python Projekte\selenium\scrap.bat'])

    # with urllib.request.urlopen(site) as url:
    #     data = url.read().decode()
    #     print(data)

    with open(r"C:\Users\Jonas\Documents\Python Projekte\selenium\postscrape\api.txt", "r") as f:
        text = f.read()

    # filters = json.dumps(text["searchedProducts"])
    # filterd1 = json.loads(filters)
    # featuredProduct = json.dumps(filterd1['featuredProduct'])
    # filterd2 = json.loads(featuredProduct)
    # print(filters)
    # retailers = json.dumps(filterd2['retailers'])
    # filterd3 = json.loads(retailers)
    # purchaseLink = json.dumps(filterd3[0]['purchaseLink'])

    m = re.search("\"purchaseLink\"\s*:\s*\"([^\"]*)\"", text)

    return m.group(1)

print(getLinkRTX3000(url_rtx3080))


