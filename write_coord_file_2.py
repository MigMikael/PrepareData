"""
1|37,54|3199,27|3206,2276|21,2243
2|43,104|3168,80|3196,2293|24,2293
3|34,81|3177,48|3190,2295|14,2253

"""

# target_device = "iPadMini4"
# target_device = "MotoC"
target_device = "S8+"

dest_path = "D:\\Documents\\Thesis\\" + target_device + "\\additional_img\\crop_img\\"

with open(dest_path + "coord.txt", 'a') as txt_file:
    for i in range(10):
        line = str(i+1) + "|,|,|,|,"
        if i != 9:
            line += "\n"
        txt_file.write(line)
    print("Finish")
