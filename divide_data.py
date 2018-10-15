from random import shuffle

train_ratio = 80
test_ratio = 20
folder_name = "S8_MotoC"

device_data = "D:\\Documents\\Thesis\\" + folder_name + "\\S8_MotoC_plus_data_6.txt"
output_train_data = "D:\\Documents\\Thesis\\" + folder_name + "\\S8_MotoC_plus_train_data_6.txt"
output_test_data = "D:\\Documents\\Thesis\\" + folder_name + "\\S8_MotoC_plus_test_data_6.txt"

data_file = open(device_data, "r")
data_list = data_file.readlines()
print("Finish Read File")

shuffle(data_list)
print("Finish Shuffle data")

length = len(data_list)
#print(length)
train_length = int(length * (train_ratio/100))
test_length = int(length * (test_ratio/100))
print("Train : ", train_length)
print("Test : ", test_length)
print("Finish Divide data")

print("Train Length", train_length)
print("Test Length", test_length)


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