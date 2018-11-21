import cv2
import os

#im_path = "D:\\Documents\\Thesis\\cifar-10-addtional\\iPad\\automobile\\IMG_1555.JPG"
image_path = "D:\\Documents\\Thesis\\cifar-10-addtional\\S8\\"

choose_img_path = image_path
h = 3024
w = 4032
count = 1

for filename in os.listdir(choose_img_path):
    if filename.endswith('jpg'):
        img = cv2.imread(choose_img_path + filename)
        t = int((w - h) / 2)
        crop_img = img[0:h, t:t+h]  # center crop

        newx, newy = (crop_img.shape[1] * 32) / h, (crop_img.shape[0] * 32) / h
        new_image = cv2.resize(crop_img, (int(newx), int(newy)))

        new_filename, extension = filename.split(".")
        cv2.imwrite(choose_img_path + "resize_img\\" + str(count) + ".jpg", new_image)
        print(filename, "Finish")
        count += 1