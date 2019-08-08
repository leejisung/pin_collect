import random
from selenium import webdriver
image_count = 5
juso = 'https://www.pinterest.co.kr/starseed13/%EB%AA%A8%EC%97%90/'


driver = webdriver.Chrome('chromedriver')
driver.get(juso)
images = driver.find_elements_by_tag_name('img')
len_img = len(images)
               

img_arr = []
for image in images:
    img_arr+=[image.get_attribute('src')]
del images[0]

    
num_images = [random.randint(0,len_img)]
while len(num_images)!=image_count:
    rand=random.randint(0,len_img)
    for i in(range(len(num_images))):        
        if rand == num_images[i]:
            break
        if i == len(num_images)-1:
            num_images+=[rand]


for i in num_images:
    images[i].screenshot((str(i)+"images")+".png")





