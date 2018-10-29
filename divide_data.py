from random import shuffle
from collections import defaultdict

train_ratio = 60
test_ratio = 20
vali_ratio = 20
folder_name = "data_2"

device_data = "D:\\Documents\\Thesis\\" + folder_name + "\\S8_MotoC_plus_data_7.txt"
output_train_data = "D:\\Documents\\Thesis\\" + folder_name + "\\S8_MotoC_plus_train_data_7.txt"
output_test_data = "D:\\Documents\\Thesis\\" + folder_name + "\\S8_MotoC_plus_test_data_7.txt"
output_vali_data = "D:\\Documents\\Thesis\\" + folder_name + "\\S8_MotoC_plus_vali_data_7.txt"

data_file = open(device_data, "r")
data_list = data_file.readlines()
shuffle(data_list)
print("### Finish Read File")

all_list = []
for item in data_list:
    item = item.replace("\n", "")
    item = item.replace("|labels ", "")
    item = item.replace("features", "")

    label, feature = item.split(" | ")
    all_list.append((feature, label))

print(all_list[:3])
d = defaultdict(list)
for f, l in all_list:
    d[f].append(l)

count = 0
for key in d:
    if count == 5:
        break
    print(key, "=>", d[key])
    count += 1

length = len(d)
print("Unique Feature : ", length)

#print(length)
train_length = int(length * (train_ratio/100))
test_length = int(length * (test_ratio/100))
vali_length = int(length * (vali_ratio/100))
print("Unique Train : ", train_length)
print("Unique Test : ", test_length)
print("Unique Vali : ", vali_length)

count = 0
count_total = 0

vali_list = []
train_test_list = []

for key in d:
    for item in d[key]:
        line = "|label " + item + " |features " + key + "\n"
        if count <= vali_length:
            vali_list.append(line)
        else:
            train_test_list.append(line)
    count += 1
print("### Finish Divide Data")

shuffle(vali_list)
shuffle(train_test_list)
print("### Finish Shuffle data")

print("vali_list : ", len(vali_list))
#print("train_test_list : ", len(train_test_list))
test_list = train_test_list[:len(vali_list)]
train_list = train_test_list[len(vali_list):]
print("test_list : ", len(test_list))
print("train_list : ", len(train_list))

with open(output_vali_data, "a") as vali_file:
    for line in vali_list:
        vali_file.write(line)
print("### Finish Write Validate File")

with open(output_test_data, "a") as test_file:
    for line in test_list:
        test_file.write(line)
print("### Finish Write Test File")

with open(output_train_data, "a") as train_file:
    for line in train_list:
        train_file.write(line)
print("### Finish Write Train File")
