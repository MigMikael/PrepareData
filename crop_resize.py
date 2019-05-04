import cv2
import os

#im_path = "D:\\Documents\\Thesis\\cifar-10-addtional\\iPad\\automobile\\IMG_1555.JPG"
#image_path = "D:\\Documents\\Thesis\\cifar-10-addtional-filter\\S8\\"
image_path = "C:\\Users\\Mig\\Documents\\cifar-10-addtional-filter\\S8\\"

choose_img_path = image_path
#h = 1920
#w = 2560
count = 1

for filename in os.listdir(choose_img_path):
    if filename.endswith('jpg') or filename.endswith('JPG'):
        img = cv2.imread(choose_img_path + filename)
        h, w, channels = img.shape

        if h != w:
            t = int((w - h) / 2)
            crop_img = img[0:h, t:t+h]  # center crop

            newx, newy = (crop_img.shape[1] * 32) / h, (crop_img.shape[0] * 32) / h
            new_image = cv2.resize(crop_img, (int(newx), int(newy)), interpolation=cv2.INTER_AREA)

        else:
            newx, newy = (img.shape[1] * 32) / h, (img.shape[0] * 32) / h
            new_image = cv2.resize(img, (int(newx), int(newy)), interpolation=cv2.INTER_AREA)

        new_filename, extension = filename.split(".")
        #cv2.imwrite("D:\\Documents\\Thesis\\cifar-10-addtional-filter\\S8_resize_2\\" + str(count) + ".jpg", new_image)
        cv2.imwrite("C:\\Users\\Mig\\Documents\\cifar-10-addtional-filter\\S8_resize_INTER_AREA_pure\\" + str(count) + ".jpg", new_image)
        th, tw, tc = new_image.shape

        is_correct = True
        if th != 32 and tw != 32:
            is_correct = False

        if is_correct:
            print(filename, "Finish")
        else:
            print(filename, "######")
        # if th != tw:
        #     is_correct = False
        # print(filename, is_correct)

        count += 1