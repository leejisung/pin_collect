import random
from selenium import webdriver
image_count = 5
juso = 'https://www.pinterest.co.kr/starseed13/%EB%AA%A8%EC%97%90/'
#rehu

driver = webdriver.Chrome('chromedriver')
driver.get(juso)
images = driver.find_elements_by_tag_name('img')
len_img = len(images)

img_arr = []
for image in images:
    img_arr+=[image.get_attribute('src')]
del images[0]

    
three_images = [random.randint(0,len_img)]
while len(three_images)!=image_count:
    rand=random.randint(0,len_img)
    for i in(range(len(three_images))):        
        if rand == three_images[i]:
            break
        if i == len(three_images)-1:
            three_images+=[rand]
print(three_images)

for i in range(image_count):
    three_images[i] = img_arr[i]


print(three_images)





