import urllib.request
import time
import random
from selenium import webdriver
image_count = 5
#juso = 'https://www.pinterest.co.kr/mornthadtartee/%E0%B8%AD%E0%B8%B0%E0%B8%99%E0%B9%80%E0%B8%A1%E0%B8%B0/'
juso = 'https://www.pinterest.co.kr/starseed13/%EB%AA%A8%EC%97%90/'

driver = webdriver.Chrome('chromedriver')
driver.get(juso)

title_ = driver.title
for i in range(len(title_)):
    if title_[i]== '이' and title_[i+1]== '미' and title_[i+2]== '지':
        number_start = i+4
        break
pin_number = ''

for i in range(number_start, len(title_)):
    if title_[i]!= '개':
        pin_number+=title_[i]
    else:
        break
pin_number = int(pin_number)

for i in range(5):
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
    urllib.request.urlretrieve(img_arr[i], "img"+str(i)+".png")





