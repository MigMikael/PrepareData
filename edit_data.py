target_device = "S8+"
# target_device = "iPadMini4"

data_path1 = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_3\\data.txt"
data_path2 = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_2\\data.txt"
dest_path = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_3\\final-data.txt"
pixel_list = []

count = 1
with open(data_path1, 'r') as data:
    for line in data:
        if count <= 14323680:
            pixel_list.append(line)
        count += 1

count = 1
with open(data_path2, 'r') as data:
    for line in data:
        if count > 14323680:
            pixel_list.append(line)
        count += 1

print(len(pixel_list))

with open(dest_path, 'w') as outfile:
    for i in range(len(pixel_list)):
        outfile.write(pixel_list[i])

print("Finish")