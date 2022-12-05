import asyncio
import os
from pyppeteer import launch
import time
import datetime
import cv2
from main_2 import *
import numpy as np
from mysql_test import *

def rotate_img(img):
    (h, w, d) = img.shape 
    center = (w // 2, h // 2) 
    
    M = cv2.getRotationMatrix2D(center, -60, 1.0)
    
    rotate_img = cv2.warpAffine(img, M, (w, h))
    
    return rotate_img

class Webscreenshooter():
    def gen_output_path(self, from_url, output_dir, file_name_manual):
        base_name = from_url.replace('.html', '').split('/')[-1]
        # file_name = "{}.png".format(base_name)
        output_path = os.path.join(output_dir, file_name_manual)
        return output_path, file_name_manual

    async def screenshot(self, url, output_path):
        browser = await launch(args=['--no-sandbox'])
        page = await browser.newPage()
        await page.setViewport({'width': 2000, 'height': 1000})
        await page.goto(url)
        time.sleep(10)
        await page.screenshot({'path': output_path})
        await browser.close()

    def take_screenshot(self, url, output_path):
        asyncio.get_event_loop().run_until_complete(self.screenshot(url, output_path))
        print('web screenshot complete')

def executeSomething():
    # nowTime = int(time.time())
    # struct_time = time.localtime(nowTime) 
    # timeString = time.strftime("%Y-%m-%d_%I:%M:%S", struct_time) 
    # print("start--",timeString)
    
    time_screenshot = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ws = Webscreenshooter()
    url = 'http://121.125.133.92:8000/webcapture.jpg?command=snap&channel=1?1655799438'
    output_dir = './screenshot/'

    output_path, file_name = ws.gen_output_path(url, output_dir, "1_cctv.png")
    ws.take_screenshot(url, output_path)
    print(output_path, file_name)

    ws = Webscreenshooter()
    url = 'http://220.157.160.198:8080/viewer/live/index.html'
    output_dir = './screenshot/'

    output_path, file_name = ws.gen_output_path(url, output_dir, "2_cctv.png")
    ws.take_screenshot(url, output_path)
    print(output_path, file_name)
    return time_screenshot

def crop_stageI():
    img_path = os.path.join('screenshot','1_cctv.png')
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img_t = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(img_t)
    v1 = np.clip(cv2.add(1*v,30),0,255)
    img = np.uint8(cv2.merge((h,s,v1)))
    img = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    x = 115
    y = 196
    w = 1773
    h = 797
    crop_img = img[y:y+h, x:x+w]
    #crop_img = rotate_img(crop_img)
    cv2.imwrite(os.path.join('screenshot','1_cctv_crop.png'), crop_img)

    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    img_path = os.path.join('screenshot','2_cctv.png')
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    img_t = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(img_t)
    v1 = np.clip(cv2.add(1*v,30),0,255)
    img = np.uint8(cv2.merge((h,s,v1)))
    img = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
    x = 34
    y = 55
    w = 1156
    h = 717
    crop_img = img[y:y+h, x:x+w]
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(os.path.join('screenshot', '2_cctv_crop.png'), crop_img)

def crop150_one():
    print("Crop cctv1 18 cars 150")
    xylist = [[33,148],[170,154],[275,154],[380,184],[493,185],[607,185], [731,143],[832,196],[955,177], [1057,181],[1172,192],[1257,203], [1370,218],[1463,232],[1555,230], [1651,203],[170,388],[1448,422]]
    x2y2list = [[117,387],[242,404],[349,397],[469,398],[592,407],[706,404], [822,366],[935,367],[1041,322], [1156,373],[1257,376],[1357,408], [1451,416],[1552,413],[1636,413], [1714,419],[500,562],[1693,538]]
    save_dir = os.path.join('testing','1_cctv')
    img_path = os.path.join('screenshot','1_cctv_crop.png')
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    for i in range(18):
        output_name = '1_cctv_'+str(i)+'.png'
        x = xylist[i][0]
        y = xylist[i][1]
        w = x2y2list[i][0] - x 
        h = x2y2list[i][1] - y
        crop_img = img[y:y+h, x:x+w]
        crop_img_150 = cv2.resize(crop_img, (256, 256), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(save_dir, output_name), crop_img_150)

def crop150_two():
    print("Crop cctv2 7 cars 150")
    xylist = [[120,127],[215,118],[317,107],[432,113],[530,117],[111,423],[408,411]]
    whlist = [[75,64],[89,57],[95,71],[75,44],[49,31],[248,286],[187,238]]
    save_dir = os.path.join('testing','2_cctv')
    img_path = os.path.join('screenshot','2_cctv_crop.png')
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    for i in range(7):
        output_name = '2_cctv_'+str(i)+'.png'
        x = xylist[i][0]
        y = xylist[i][1]
        w = whlist[i][0]
        h = whlist[i][1]
        crop_img = img[y:y+h, x:x+w]
        crop_img_150 = cv2.resize(crop_img, (256, 256), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(save_dir, output_name), crop_img_150)

def processing_result(parking_result, total, time_screenshot, area):
    ava = 0
    for a in parking_result:
        if a == 0:
            ava+=1
    noava = total - ava
    print("Time stamp: ", time_screenshot)
    print("Avalible: ", ava)
    print("Occupied: ", noava) 
    if area == 1:
        writetoDB_korea(time_screenshot, ava, noava)
    else:
        writetoDB_japan(time_screenshot, ava, noava)


if __name__ == '__main__':

    while True:
        print("Start Task")
        time_screenshot = executeSomething()
        print("finish--", time_screenshot)
        #time_screenshot = 'test'
        crop_stageI()
        crop150_one()
        crop150_two()
        parking_result = run_testing_task('testing/1_cctv/', 'testing/1_cctv_testing.txt')
        processing_result(parking_result, 18, time_screenshot, 1)
        parking_result = run_testing_task('testing/2_cctv/', 'testing/2_cctv_testing.txt')
        processing_result(parking_result, 7, time_screenshot, 2)
        print("sleep start 5 mins")
        time.sleep(300)
        print("sleep end")


    # time_screenshot = executeSomething()
    # print("finish--", time_screenshot)
    # # time_screenshot = 'test'
    # crop_stageI()
    # crop150_one()
    # crop150_two()
    # parking_result = run_testing_task('testing/1_cctv/', 'testing/1_cctv_testing.txt')
    # processing_result(parking_result, 18, time_screenshot, 1)
    # parking_result = run_testing_task('testing/2_cctv/', 'testing/2_cctv_testing.txt')
    # processing_result(parking_result, 7, time_screenshot, 2)


