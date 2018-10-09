import cv2
import math

region = 7
# target_device = "S8+"
# target_device = "iPadMini4"
# target_device = "MotoC"
target_device = "Mi5"

# data_path = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_2\\crop\\"
data_path = "D:\\Documents\\Thesis\\" + target_device + "\\data_set_3\\"


def draw_rect(img, tl, tr, br, bl):
    cv2.rectangle(img, (tl, tr), (br, bl), (255, 255, 255), 1)
    return img


def crop_img(img, y, yr, x, xr):
    cropp = img[y:yr, x:xr]
    cropp = cv2.cvtColor(cropp, cv2.COLOR_BGR2RGB)
    return cropp


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
                distance = math.sqrt((r_bar - item[0])**2 + (g_bar - item[1])**2 + (b_bar - item[2])**2)
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


def plot_coordinate(img, edit_image, region):
    pixel_list = []
    centerX = 10
    centerY = 7
    for i in range(20):
        for j in range(14):

            diffX = abs(centerX - i)
            diffY = abs(centerY - j)
            if diffX > diffY:
                dist = diffX
            else:
                dist = diffY

            indexX, indexY = 6 + (42 * i) - (i * 2), 8 + (44 * j) - j

            if i <= 10:
                indexX = indexX
            else:
                indexX = indexX

            if i > 17:
                indexX = indexX - 2

            index_sq1_x, index_sq1_y = indexX, indexY
            index_sq2_x, index_sq2_y = indexX + 9, indexY
            index_sq3_x, index_sq3_y = indexX + 18, indexY

            index_sq4_x, index_sq4_y = indexX, indexY + 9
            index_sq5_x, index_sq5_y = indexX + 9, indexY + 9
            index_sq6_x, index_sq6_y = indexX + 18, indexY + 9

            index_sq7_x, index_sq7_y = indexX, indexY + 18
            index_sq8_x, index_sq8_y = indexX + 9, indexY + 18
            index_sq9_x, index_sq9_y = indexX + 18, indexY + 18

            edit_image = draw_rect(edit_image, index_sq1_x, index_sq1_y, index_sq1_x + region, index_sq1_y + region)
            edit_image = draw_rect(edit_image, index_sq2_x, index_sq2_y, index_sq2_x + region, index_sq2_y + region)
            edit_image = draw_rect(edit_image, index_sq3_x, index_sq3_y, index_sq3_x + region, index_sq3_y + region)
            edit_image = draw_rect(edit_image, index_sq4_x, index_sq4_y, index_sq4_x + region, index_sq4_y + region)
            edit_image = draw_rect(edit_image, index_sq5_x, index_sq5_y, index_sq5_x + region, index_sq5_y + region)
            edit_image = draw_rect(edit_image, index_sq6_x, index_sq6_y, index_sq6_x + region, index_sq6_y + region)
            edit_image = draw_rect(edit_image, index_sq7_x, index_sq7_y, index_sq7_x + region, index_sq7_y + region)
            edit_image = draw_rect(edit_image, index_sq8_x, index_sq8_y, index_sq8_x + region, index_sq8_y + region)
            edit_image = draw_rect(edit_image, index_sq9_x, index_sq9_y, index_sq9_x + region, index_sq9_y + region)

            sq1_crop = crop_img(img, index_sq1_y, index_sq1_y + region, index_sq1_x, index_sq1_x + region)
            sq2_crop = crop_img(img, index_sq2_y, index_sq2_y + region, index_sq2_x, index_sq2_x + region)
            sq3_crop = crop_img(img, index_sq3_y, index_sq3_y + region, index_sq3_x, index_sq3_x + region)
            sq4_crop = crop_img(img, index_sq4_y, index_sq4_y + region, index_sq4_x, index_sq4_x + region)
            sq5_crop = crop_img(img, index_sq5_y, index_sq5_y + region, index_sq5_x, index_sq5_x + region)
            sq6_crop = crop_img(img, index_sq6_y, index_sq6_y + region, index_sq6_x, index_sq6_x + region)
            sq7_crop = crop_img(img, index_sq7_y, index_sq7_y + region, index_sq7_x, index_sq7_x + region)
            sq8_crop = crop_img(img, index_sq8_y, index_sq8_y + region, index_sq8_x, index_sq8_x + region)
            sq9_crop = crop_img(img, index_sq9_y, index_sq9_y + region, index_sq9_x, index_sq9_x + region)

            pixel_list = collect_pixel_data2(sq1_crop, pixel_list)
            pixel_list = collect_pixel_data2(sq2_crop, pixel_list)
            pixel_list = collect_pixel_data2(sq3_crop, pixel_list)
            pixel_list = collect_pixel_data2(sq4_crop, pixel_list)
            pixel_list = collect_pixel_data2(sq5_crop, pixel_list)
            pixel_list = collect_pixel_data2(sq6_crop, pixel_list)
            pixel_list = collect_pixel_data2(sq7_crop, pixel_list)
            pixel_list = collect_pixel_data2(sq8_crop, pixel_list)
            pixel_list = collect_pixel_data2(sq9_crop, pixel_list)

    return pixel_list, edit_image


def write_file(file_name, the_list):
    with open(file_name, 'a') as outfile:
        for i in range(len(the_list)):
            data_line = str(the_list[i][0]) + " " + str(the_list[i][1]) + " " + str(the_list[i][2])
            data_line = data_line + "\n"
            outfile.write(data_line)
    #print("wrote file")


for i in range(30):
    for j in range(4):
        filename = data_path + "trans_img_" + str(i + 1) + "_" + str(j + 1) + ".jpg"

        img = cv2.imread(filename)
        edit_image = img.copy()

        device_pixel_list, edit_image = plot_coordinate(img, edit_image, region)

        dest_path = data_path + str(i+1) + "-" + str(j+1) + ".jpg"
        cv2.imwrite(dest_path, edit_image)

        output_path = data_path + "data_centroid_2.txt"
        write_file(output_path, device_pixel_list)
        print("Finish " + filename)



