import cv2


region = 7
# target_device = "S8+"
target_device = "iPadMini4"

# data_path = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_2\\crop\\"
data_path = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_3\\"


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
                indexX = indexX + (dist // 3)

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

            pixel_list = collect_pixel_data(sq1_crop, pixel_list)
            pixel_list = collect_pixel_data(sq2_crop, pixel_list)
            pixel_list = collect_pixel_data(sq3_crop, pixel_list)
            pixel_list = collect_pixel_data(sq4_crop, pixel_list)
            pixel_list = collect_pixel_data(sq5_crop, pixel_list)
            pixel_list = collect_pixel_data(sq6_crop, pixel_list)
            pixel_list = collect_pixel_data(sq7_crop, pixel_list)
            pixel_list = collect_pixel_data(sq8_crop, pixel_list)
            pixel_list = collect_pixel_data(sq9_crop, pixel_list)

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

        output_path = data_path + "data.txt"
        write_file(output_path, device_pixel_list)
        print("Finish " + filename)



