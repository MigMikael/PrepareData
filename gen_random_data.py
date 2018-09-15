import cv2
import numpy as np
from random import randint, shuffle

font = cv2.FONT_HERSHEY_SIMPLEX

# choose color that not factor of 8
color_list = []
for i in range(256):
    for j in range(256):
        for k in range(256):
            if i % 8 != 0 and j % 8 != 0 and k % 8 != 0:
                color_list.append([i, j, k])

print(len(color_list))

# Since output image has (40 * 28 = 1120) * 10 = 11,200 pattern
# we have to randomly select 11,200 color from our "color_list"
# len(color_list) = 11239424
# therefore 11239424 / 11200 = 1003.52
choose_color_list = []
for i in range(0, len(color_list)-1003, 1003):
    position = randint(i, i+1003)
    choose_color_list.append(color_list[position])

print(len(choose_color_list))
print(choose_color_list[:5])

# len(choose_color) = 11,205 randomly remove five color
for i in range(5):
    pop_index = randint(0, len(choose_color_list))
    choose_color_list.pop(pop_index)

# a little bit of shuffle
print(len(choose_color_list))
shuffle(choose_color_list)

# then we write the output image
for k in range((len(choose_color_list) // 1120)+1):
    img_name = "shuffle_image_"+str(k+1)+".png"
    save_path = "D:\\Documents\\Thesis\\Random_Color\\"
    height, width = 2480, 3508  # A4 paper 300 PPI
    the_image = np.zeros((height, width, 3), np.uint8)
    the_image[:, 0:width] = (255, 255, 255)  # (B, G, R)

    cv2.rectangle(the_image, (5, 5), (3503, 2475), (0, 0, 0), 5)

    count = 0
    for i in range(40):
        for j in range(28):
            # print((320*k) + count)
            index = (1120 * k) + count
            if index >= len(choose_color_list):
                R, G, B = 255, 255, 255
            else:
                R = choose_color_list[index][0]
                G = choose_color_list[index][1]
                B = choose_color_list[index][2]
                # print(R, G, B)

            cv2.rectangle(the_image, (30 + (85 * i), 30 + (85 * j)), (107 + (85 * i), 107 + (85 * j)), (B, G, R),
                          -1)
            count += 1
    cv2.putText(the_image, str(k + 1), (3443, 70), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imwrite(save_path + img_name, the_image)
    print("Finish write " + img_name)
    #break

print("Finish")