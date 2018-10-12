import cv2
import math

sx, sy = 0, 0

region = 7
target_device = "S8+"
# target_device = "iPadMini4"
# target_device = "MotoC"
# target_device = "Mi5"

data_path = "D:\\Documents\\Thesis\\" + target_device + "\\additional_img\\crop_img\\"
coord_path = data_path + "coord.txt"
dest_file_name = "data.txt"


def greetings():
    print("Welcome to additional auto region picker")


def read_image(path):
    img = cv2.imread(path)
    return img


def plot_coordinate(img, x, y, region, num):
    edit_img = img.copy()
    startX = x
    startY = y
    count = 0
    pixel_list = []

    for i in range(6):
        for j in range(5):
            indexX, indexY = startX + 100 + (270 * i), startY + 90 + (250 * j)

            index_sq1_x, index_sq1_y = indexX, indexY
            index_sq2_x, index_sq2_y = indexX + 14, indexY
            index_sq3_x, index_sq3_y = indexX + 28, indexY

            index_sq4_x, index_sq4_y = indexX, indexY + 14
            index_sq5_x, index_sq5_y = indexX + 14, indexY + 14
            index_sq6_x, index_sq6_y = indexX + 28, indexY + 14

            index_sq7_x, index_sq7_y = indexX, indexY + 28
            index_sq8_x, index_sq8_y = indexX + 14, indexY + 28
            index_sq9_x, index_sq9_y = indexX + 28, indexY + 28


            cv2.rectangle(edit_img, (index_sq1_x, index_sq1_y), (index_sq1_x + region, index_sq1_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq2_x, index_sq2_y), (index_sq2_x + region, index_sq2_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq3_x, index_sq3_y), (index_sq3_x + region, index_sq3_y + region),
                          (255, 255, 255), 1)

            cv2.rectangle(edit_img, (index_sq4_x, index_sq4_y), (index_sq4_x + region, index_sq4_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq5_x, index_sq5_y), (index_sq5_x + region, index_sq5_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq6_x, index_sq6_y), (index_sq6_x + region, index_sq6_y + region),
                          (255, 255, 255), 1)

            cv2.rectangle(edit_img, (index_sq7_x, index_sq7_y), (index_sq7_x + region, index_sq7_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq8_x, index_sq8_y), (index_sq8_x + region, index_sq8_y + region),
                          (255, 255, 255), 1)
            cv2.rectangle(edit_img, (index_sq9_x, index_sq9_y), (index_sq9_x + region, index_sq9_y + region),
                          (255, 255, 255), 1)


            sq1_crop = img[index_sq1_y:index_sq1_y + region, index_sq1_x:index_sq1_x + region]
            sq1_crop = cv2.cvtColor(sq1_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq1_crop, pixel_list)

            sq2_crop = img[index_sq2_y:index_sq2_y + region, index_sq2_x:index_sq2_x + region]
            sq2_crop = cv2.cvtColor(sq2_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq2_crop, pixel_list)

            sq3_crop = img[index_sq3_y:index_sq3_y + region, index_sq3_x:index_sq3_x + region]
            sq3_crop = cv2.cvtColor(sq3_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq3_crop, pixel_list)

            sq4_crop = img[index_sq4_y:index_sq4_y + region, index_sq4_x:index_sq4_x + region]
            sq4_crop = cv2.cvtColor(sq4_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq4_crop, pixel_list)

            sq5_crop = img[index_sq5_y:index_sq5_y + region, index_sq5_x:index_sq5_x + region]
            sq5_crop = cv2.cvtColor(sq5_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq5_crop, pixel_list)

            sq6_crop = img[index_sq6_y:index_sq6_y + region, index_sq6_x:index_sq6_x + region]
            sq6_crop = cv2.cvtColor(sq6_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq6_crop, pixel_list)

            sq7_crop = img[index_sq7_y:index_sq7_y + region, index_sq7_x:index_sq7_x + region]
            sq7_crop = cv2.cvtColor(sq7_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq7_crop, pixel_list)

            sq8_crop = img[index_sq8_y:index_sq8_y + region, index_sq8_x:index_sq8_x + region]
            sq8_crop = cv2.cvtColor(sq8_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq8_crop, pixel_list)

            sq9_crop = img[index_sq9_y:index_sq9_y + region, index_sq9_x:index_sq9_x + region]
            sq9_crop = cv2.cvtColor(sq9_crop, cv2.COLOR_BGR2RGB)
            pixel_list = collect_pixel_data2(sq9_crop, pixel_list)


            count += 1
    print(len(pixel_list))
    return pixel_list, edit_img


def collect_pixel_data(tiny_crop, pixel_list):
    for k in range(tiny_crop.shape[0]):
        for l in range(tiny_crop.shape[1]):
            r = tiny_crop[k][l][0]
            g = tiny_crop[k][l][1]
            b = tiny_crop[k][l][2]
            pixel_list.append([r, g, b])

    return pixel_list


def takeLast(elem):
    return elem[-1]


def collect_pixel_data2(tiny_crop, pixel_list):
    for k in range(1, 6):  # 1 2 3 4 5
        for l in range(1, 6):  # 1 2 3 4 5
            center_x = k
            center_y = l
            region_list = []
            sum_r, sum_g, sum_b = 0, 0, 0
            for m in range(center_x - 1, center_x + 2):
                for n in range(center_y - 1, center_y + 2):
                    r = tiny_crop[m][n][0]
                    g = tiny_crop[m][n][1]
                    b = tiny_crop[m][n][2]
                    sum_r += r
                    sum_g += g
                    sum_b += b
                    region_list.append([r, g, b, 0])

            r_bar = int(round(sum_r / float(9)))
            g_bar = int(round(sum_g / float(9)))
            b_bar = int(round(sum_b / float(9)))

            for item in region_list:
                distance = math.sqrt((r_bar - item[0]) ** 2 + (g_bar - item[1]) ** 2 + (b_bar - item[2]) ** 2)
                item[3] = distance

            region_list.sort(key=takeLast)
            region_list = region_list[0:3]

            r_sum = 0
            g_sum = 0
            b_sum = 0
            for item in region_list:
                r_sum += item[0]
                g_sum += item[1]
                b_sum += item[2]
            avg_r = r_sum // 3
            avg_g = g_sum // 3
            avg_b = b_sum // 3
            pixel_list.append([int(avg_r), int(avg_g), int(avg_b)])

    return pixel_list


def collect_pixel_data3(tiny_crop, pixel_list):
    r, g, b = 0, 0, 0
    for k in range(tiny_crop.shape[0]):
        for l in range(tiny_crop.shape[1]):
            r += tiny_crop[k][l][0]
            g += tiny_crop[k][l][1]
            b += tiny_crop[k][l][2]

    r = int(round(r / float(49)))
    g = int(round(g / float(49)))
    b = int(round(b / float(49)))
    pixel_list.append([r, g, b])

    return pixel_list


def write_file(file_name, the_list):
    with open(file_name, 'a') as outfile:
        for i in range(len(the_list)):
            data_line = str(the_list[i][0]) + " " + str(the_list[i][1]) + " " + str(the_list[i][2])
            data_line = data_line + "\n"
            outfile.write(data_line)
    # print("wrote file")


def write_image(write_path, image):
    cv2.imwrite(write_path, image)


greetings()

with open(coord_path, 'r')as data_file:
    for line in data_file:
        no, w, x, y, z = line.split("|")

        img_name = "trans_img_" + no

        dev_img_path = data_path + img_name + ".jpg"
        device_img = read_image(dev_img_path)

        device_pixel_list, edit_image = plot_coordinate(device_img, 0, 0, region, int(no))

        write_image(data_path + img_name + "_plot.jpg", edit_image)

        write_file(data_path + dest_file_name, device_pixel_list)

        print("Finish Image", no)

    print("Finish -------------")
