#Site used: https://www.webtoolhub.com/
import sys
from time import sleep
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def image(imgs):
    print(Fore.RED + """
    ------ Image ------
           -----
    """)

    count = 0
    for img in imgs[1:]:
        count += 1
        print(str(count) + ": " + str(img.text[2:]).replace("\n", ""))

def javascript(javas):
    print(Fore.RED + """
    ------ JavaScript ------
           ----------
    """)

    count = 0
    for js in javas[1:]:
        count += 1
        print(str(count) + ": " + str(js.text[2:]).replace("\n", ""))

def general(gnrl):
    print(Fore.RED + """
    ------ General ------
           -------
    """)

    count = 0
    for gn in gnrl[1:]:
        count += 1
        print(str(count) + ": " + str(gn.text[2:]).replace("\n", ""))

if __name__ == '__main__':
    print(Fore.GREEN + """
    WWWWWWWWWWWWWWWWWWWWWWWWWWWNKkxdx0XWWWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWWWNXOl'.....;xXWWWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWWNKdc;..,lo:...:0WWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWWWWNX0O00OkKWWNx' .lXWWWWWWWWWWW
    WWWWWWWWWWWWWWWWWWNOo:,,;:lkXWWNKo. .oNWWWWWWWWWWW
    WWWWWWWWWWWWWWWWNOc....'...'xNKd,..'oKWWWWWWWWWWWW
    WWWWWWWWWWWWWWNOl...,d0KkddO0d,..'l0NWWWWWWWWWWWWW
    WWWWWWWWWWWWNOl...,d00KNWNKd,...l0NWWWWWWWWWWWWWWW
    WWWWWWWWWWN0l'..,dK0c.'cc:,...l0NWWWWWWWWWWWWWWWWW
    WWWWWWWWWWO;..,dKNNKo;.....,l0NWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWNd. .dNWWNXXK0kkO0XNWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWW0;..'oOOo;,:o0NWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWKo'......'l0NWWWWWWWWWWWWWWWWWWWWWWWWWW
    WWWWWWWWWWWWNOc....:kNWWWWWWWWWWWWWWWWWWWWWWWWWWWW
    """)
    print(Fore.YELLOW + "Waiting..")

    opt = Options()
    opt.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="driver/chromedriver.exe", options=opt)
    driver.get("https://www.webtoolhub.com/tn561364-link-extractor.aspx")

    url = input(Fore.YELLOW + "Url: ")

    urlInput = driver.find_element_by_xpath('//*[@id="ctl00_CPH1_TextBoxUrl"]')
    urlInput.send_keys(url)
    urlExt = driver.find_element_by_xpath('//*[@id="ctl00_CPH1_ButtonStart"]').click()

    images = driver.find_elements_by_xpath('//*[@id="DivResult"]/table[3]/tbody/tr')
    javascriptFiles = driver.find_elements_by_xpath('//*[@id="DivResult"]/table[4]/tbody/tr')
    generals = driver.find_elements_by_xpath('//*[@id="DivResult"]/table[5]/tbody/tr')

    image(images)
    sleep(0.5)
    javascript(javascriptFiles)
    sleep(0.5)
    general(generals)

    sleep(4)

    driver.quit()
