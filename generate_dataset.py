#generate dataset
from selenium import webdriver 
import urllib.request
import requests
import time
i = 1
driver = webdriver.Chrome("C:\\Users\\ADITYA\\chromedriver")
driver.get("http://14.139.110.183/geca/")
time.sleep(10)
while i<1000:
    i = i+1
    time.sleep(1)
    images = driver.find_elements_by_tag_name('img')
    lst = []
    for image in images:
        lst.append(image.get_attribute('src'))
    src = lst[-1]
    #print(src)
    #src =  "https://14.139.110.183/geca/" + src
    print(src)
    filename = "sample"+str(i)+".png"
    time.sleep(1)
    #urllib.request.urlretrieve(src,"C:\\Users\\ADITYA\\Desktop\\Python Scripts\\dataset\\" + filename)
    r = requests.get(src, allow_redirects=True)
    down_path = 'C:\\Users\\ADITYA\\Desktop\\Python Scripts\\dataset\\'+filename
    open(down_path, 'wb').write(r.content)
    driver.refresh()
