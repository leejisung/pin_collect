import urllib.request
import time
import random
import pandas as pd
from selenium import webdriver
image_count = 5
page_down = 5
data = pd.read_csv('data.csv', sep=',')
juso = data.site[0]

driver = webdriver.Chrome('chromedriver')
driver.get(juso)

for i in range(page_down):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

images = driver.find_elements_by_tag_name('img')
len_img = len(images)
               

img_arr = []
for image in images:
    img_arr+=[image.get_attribute('src')]
del images[0]

    
num_images = [random.randint(1,len_img)]
while len(num_images)!=image_count:
    rand=random.randint(1,len_img)
    for i in(range(len(num_images))):        
        if rand == num_images[i]:
            break
        if i == len(num_images)-1:
            num_images+=[rand]


for i in num_images:
    urllib.request.urlretrieve(img_arr[i], data.local[0]+"\\"+"img"+str(i)+".png")
