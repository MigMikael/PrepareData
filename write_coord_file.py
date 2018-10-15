# target_device = "iPadMini4"
target_device = "S8+"
# target_device = "MotoC"
# target_device = "Mi5"

dest_path = "D:\\Documents\\Thesis\\" + target_device + "\\random_color_2\\"

with open(dest_path + "coord3.txt", 'a') as txtfile:
    for i in range(10):
        line = str(i+1) + "|,|,|,|,|,|,|,|,|,"
        if i != 9:
            line += "\n"
        txtfile.write(line)
    print("Finish")
