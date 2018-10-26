from random import shuffle

train_ratio = 60
test_ratio = 20
vali_ratio = 20
folder_name = "data_2"

device_data = "D:\\Documents\\Thesis\\" + folder_name + "\\iPad_MotoC_plus_data_7.txt"
output_train_data = "D:\\Documents\\Thesis\\" + folder_name + "\\iPad_MotoC_plus_train_data_6.txt"
output_test_data = "D:\\Documents\\Thesis\\" + folder_name + "\\iPad_MotoC_plus_test_data_6.txt"
output_vali_data = "D:\\Documents\\Thesis\\" + folder_name + "\\iPad_MotoC_plus_vali_data_6.txt"

data_file = open(device_data, "r")
data_list = data_file.readlines()
print("Finish Read File")

#shuffle(data_list)
print("Finish Shuffle data")

data_dict = {}

for item in data_list:
    item = item.replace("\n", "")
    item = item.replace("|labels ", "")
    item = item.replace("features", "")

    label, feature = item.split(" | ")
    # print(label, "=", feature)

    data_dict[feature] = label

print(len(data_dict))
len_data_dict = len(data_dict)
len_collect = int(0.2 * len_data_dict)
print(len_collect)

feature_collect = []

count = 0
for key in data_dict:
    feature_collect.append("|features " + key)
    count += 1
    if count <= 5:
        print(key, "=>", data_dict[key])

    if count == len_collect:
        break

print(len(feature_collect))
print(feature_collect[:5])

count = 0
vali_list = []
for key in data_dict:
    if count == len_collect:
        break
    line = "|labels " + data_dict[key] + " |features " + key + "\n"
    vali_list.append(line)
    count += 1

print(len(vali_list))
print(vali_list[:5])
count = 0

data_list = [e for e in data_list if e not in feature_collect]

print(len(data_list))
'''
length = len(data_list)
#print(length)
train_length = int(length * (train_ratio/100))
test_length = int(length * (test_ratio/100))
vali_length = int(length * (vali_ratio/100))
print("Train : ", train_length)
print("Test : ", test_length)
print("Vali : ", vali_length)
print("Finish Divide data")

print("Train Length", train_length)
print("Test Length", test_length)
print("Validata Length", vali_length)

with open(output_train_data, "a") as train_file:
    for i in range(train_length):
        line = data_list[i]
        train_file.write(line)
print("Finish Write Train File")

with open(output_test_data, "a") as test_file:
    for i in range(test_length):
        line = data_list[train_length + i]
        test_file.write(line)
print("Finish Write Test File")
'''