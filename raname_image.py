import numpy
import cv2
import os


# target_device = "S8+"
target_device = "iPadMini4"
image_folder = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_2"

count = 1
for filename in os.listdir(image_folder):
    if filename.endswith(".JPG"):
        img = cv2.imread(image_folder + "\\" + filename)

        dest_path = image_folder + "\\" + "img_" + str(count) + ".jpg"
        cv2.imwrite(dest_path, img)
        print("Writed " + str(count))
        count += 1

