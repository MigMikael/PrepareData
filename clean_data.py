target_device1 = "iPadMini4"
target_device2 = "MotoC"
target_device3 = "S8+"

data_path1 = "D:\\Documents\\Thesis\\" + target_device1 + "\\data_set_3\\data_clean_32.txt"
data_path2 = "D:\\Documents\\Thesis\\" + target_device2 + "\\data_set_3\\data_clean_32.txt"
data_path3 = "D:\\Documents\\Thesis\\" + target_device3 + "\\data_set_3\\data_clean_32.txt"

out_path1 = "D:\\Documents\\Thesis\\" + target_device1 + "\\data_set_3\\data_clean_33.txt"
out_path2 = "D:\\Documents\\Thesis\\" + target_device2 + "\\data_set_3\\data_clean_33.txt"
out_path3 = "D:\\Documents\\Thesis\\" + target_device3 + "\\data_set_3\\data_clean_33.txt"

device_data1 = []
device_data2 = []
device_data3 = []

with open(data_path1, "r") as data_file:
    for line in data_file:
        device_data1.append(line)

with open(data_path2, "r") as data_file:
    for line in data_file:
        device_data2.append(line)

with open(data_path3, "r") as data_file:
    for line in data_file:
        device_data3.append(line)

print(len(device_data1))
print(len(device_data2))
print(len(device_data3))

len_data = len(device_data1)

count = 0
threshold = 190
abnormal_idx = []

for i in range(len_data):
    r1, g1, b1 = device_data1[i].split(" ")
    r2, g2, b2 = device_data2[i].split(" ")
    r3, g3, b3 = device_data3[i].split(" ")

    r1, g1, b1 = int(r1), int(g1), int(b1)
    r2, g2, b2 = int(r2), int(g2), int(b2)
    r3, g3, b3 = int(r3), int(g3), int(b3)

    if abs(r1 - r2) > threshold or abs(r1 - r3) > threshold or abs(r2 - r3) > threshold:
        count += 1
        abnormal_idx.append(i)
        #print("R = ", r1, r2, r3)

    if abs(g1 - g2) > threshold or abs(g1 - g3) > threshold or abs(g2 - g3) > threshold:
        count += 1
        abnormal_idx.append(i)

    if abs(b1 - b2) > threshold or abs(b1 - b3) > threshold or abs(b2 - b3) > threshold:
        count += 1
        abnormal_idx.append(i)

print(count)
abnormal_idx = set(abnormal_idx)
print(len(abnormal_idx))

for item in abnormal_idx:
    #print(item)
    device_data1.pop(item)
    device_data2.pop(item)
    device_data3.pop(item)

print(len(device_data1))
print(len(device_data2))
print(len(device_data3))

with open(out_path1, "w") as out_file:
    for item in device_data1:
        out_file.write(item)

with open(out_path2, "w") as out_file:
    for item in device_data2:
        out_file.write(item)

with open(out_path3, "w") as out_file:
    for item in device_data3:
        out_file.write(item)

print("Finish")
