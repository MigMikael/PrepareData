import numpy
import cv2


# target_device = "S8+"
target_device = "iPadMini4"
# target_device = "MotoC"
# target_device = "Mi5"

# image_path = "D:\\Documents\\Thesis\\" + target_device + "\\data_set_2\\"
image_path = "D:\\Documents\\Thesis\\" + target_device + "\\random_color\\"


def order_points(pts):
    rect = numpy.zeros((4,2), dtype="float32")
    s = pts.sum(axis=1)

    # top-left have smallest sum
    # bottom-right have largest sum
    rect[0] = pts[numpy.argmin(s)]
    rect[2] = pts[numpy.argmax(s)]

    # top-right have smallest diff
    # bottom-left have largest diff
    diff = numpy.diff(pts, axis=1)
    rect[1] = pts[numpy.argmin(diff)]
    rect[3] = pts[numpy.argmax(diff)]

    return rect


def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = numpy.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = numpy.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = numpy.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = numpy.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    dst = numpy.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped


with open(image_path + "coord3.txt", 'r') as coord_file:
    for line in coord_file:
        no, point1, point2, point3, point4, a, b, c, d, e = line.split('|')
        source_path = image_path + "img_" + no + ".jpg"
        image = cv2.imread(source_path)

        point1_x, point1_y = point1.split(',')
        point2_x, point2_y = point2.split(',')
        point3_x, point3_y = point3.split(',')
        point4_x, point4_y = point4.split(',')
        a_x, a_y = a.split(',')
        b_x, b_y = b.split(',')
        c_x, c_y = c.split(',')
        d_x, d_y = d.split(',')
        e_x, e_y = e.split(',')

        rec1 = numpy.array([
            [int(point1_x), int(point1_y)],
            [int(a_x), int(a_y)],
            [int(e_x), int(e_y)],
            [int(d_x), int(d_y)]
        ])
        warped = four_point_transform(image, rec1)
        newx, newy = (warped.shape[0] * 800) / warped.shape[0], (warped.shape[1] * 600) / warped.shape[1]
        warped_resize = cv2.resize(warped, (int(newx), int(newy)))
        dest_path = image_path + "trans_img_" + no + "_1" + ".jpg"
        cv2.imwrite(dest_path, warped_resize)

        rec2 = numpy.array([
            [int(a_x), int(a_y)],
            [int(point2_x), int(point2_y)],
            [int(b_x), int(b_y)],
            [int(e_x), int(e_y)]
        ])
        warped = four_point_transform(image, rec2)
        newx, newy = (warped.shape[0] * 800) / warped.shape[0], (warped.shape[1] * 600) / warped.shape[1]
        warped_resize = cv2.resize(warped, (int(newx), int(newy)))
        dest_path = image_path + "trans_img_" + no + "_2" + ".jpg"
        cv2.imwrite(dest_path, warped_resize)

        rec3 = numpy.array([
            [int(e_x), int(e_y)],
            [int(b_x), int(b_y)],
            [int(point3_x), int(point3_y)],
            [int(c_x), int(c_y)]
        ])
        warped = four_point_transform(image, rec3)
        newx, newy = (warped.shape[0] * 800) / warped.shape[0], (warped.shape[1] * 600) / warped.shape[1]
        warped_resize = cv2.resize(warped, (int(newx), int(newy)))
        dest_path = image_path + "trans_img_" + no + "_3" + ".jpg"
        cv2.imwrite(dest_path, warped_resize)

        rec4 = numpy.array([
            [int(d_x), int(d_y)],
            [int(e_x), int(e_y)],
            [int(c_x), int(c_y)],
            [int(point4_x), int(point4_y)]
        ])
        warped = four_point_transform(image, rec4)
        newx, newy = (warped.shape[0] * 800) / warped.shape[0], (warped.shape[1] * 600) / warped.shape[1]
        warped_resize = cv2.resize(warped, (int(newx), int(newy)))
        dest_path = image_path + "trans_img_" + no + "_4" + ".jpg"
        cv2.imwrite(dest_path, warped_resize)

        print("Finish img_" + no)
