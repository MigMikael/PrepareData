import cv2

no = 1
#target_device = "S8+"
target_device = "iPadMini4"
data_path = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_2\\"
dest_path = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_2\\crop\\"

for i in range(30):
    filename = data_path + "trans_img_" + str(no) + ".jpg"
    print(filename)
    img = cv2.imread(filename)
    #img = cv2.imread("C:\\Users\\Mig\\Documents\\Thesis\\S8+\\Arm(S8+)_resize.jpg")
    first_portion = img[0:600, 0:800]
    second_portion = img[0:600, 800:1600]
    third_portion = img[600:1200, 800:1600]
    forth_portion = img[600:1200, 0:800]

    cv2.imwrite(dest_path + "img_" + str(no) + "-1.jpg", first_portion)
    cv2.imwrite(dest_path + "img_" + str(no) + "-2.jpg", second_portion)
    cv2.imwrite(dest_path + "img_" + str(no) + "-3.jpg", third_portion)
    cv2.imwrite(dest_path + "img_" + str(no) + "-4.jpg", forth_portion)
    #break
    no += 1