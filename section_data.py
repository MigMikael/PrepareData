device_data = "C:\\Users\\Mig\\Documents\\Thesis\\iPad_s8\\iPad_s8_train_data_1.txt"

data_file = open(device_data, "r")
data_list = data_file.readlines()
length = len(data_list)
print(length)
print("Finish Read File")

dest_file_name = "C:\\Users\\Mig\\Documents\\Thesis\\iPad_s8\\iPad_s8_train_data_1-"
section_len = length // 10

for i in range(10):
    with open(dest_file_name + str(i+1) + ".txt", "a") as section_file:
        section_file.write(".")
        for j in range(section_len):
            #print(i*section_len + j)
            #break
            line = data_list[i*section_len + j]
            section_file.write(line)
    print("Finish " + str(i + 1))
