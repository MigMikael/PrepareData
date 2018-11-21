import cv2
import os


iPad_image_path = "D:\\Documents\\Thesis\\iPadMini4\\additional_img\\"
s8_image_path = "D:\\Documents\\Thesis\\S8+\\data_set\\"
motoC_image_path = "D:\\Documents\\Thesis\\MotoC\\additional_img\\"
mi5_image_path = "D:\\Documents\\Thesis\\Mi5\\additional_img\\"

image_path = "D:\\Documents\\Thesis\\cifar-10-addtional\\iPad\\automobile\\"

choose_img_path = image_path

for filename in os.listdir(choose_img_path):
    if filename.endswith('JPG'):
        original_image = cv2.imread(choose_img_path + filename)
        newx, newy = (original_image.shape[1] * 32) / 2448, (original_image.shape[0] * 32) / 3264
        #newx, newy = (original_image.shape[1] * 1200) / 3024, (original_image.shape[0] * 1600) / 4032
        #newx, newy = (original_image.shape[1] * 1200) / 1920, (original_image.shape[0] * 1600) / 2560
        #newx, newy = (original_image.shape[1] * 1200) / 3456, (original_image.shape[0] * 1600) / 4608
        new_image = cv2.resize(original_image, (int(newx), int(newy)))
        new_filename, extension = filename.split(".")
        cv2.imwrite(choose_img_path + "resize_img\\" + new_filename + ".jpg", new_image)
        print(filename, "Finish")
