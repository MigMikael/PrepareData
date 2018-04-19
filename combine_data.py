

label_device = "iPadMini4"
feature_device = "S8+"

base_path = "C:\\Users\\Mig\\Documents\\Thesis\\"
label_data = base_path + label_device + "\\data_set_2\\data.txt"
feature_data = base_path + feature_device + "\\data_set_2\\data.txt"
output_data = "C:\\Users\\Mig\\Documents\\Thesis\\iPad_s8\\iPad_S8_data_1.txt"

label_file = open(label_data, "r")
feature_file = open(feature_data, "r")

label_RGB_list = label_file.readlines()
feature_RGB_list = feature_file.readlines()

length = len(label_RGB_list)
print("Label : ", length)

length2 = len(feature_RGB_list)
print("Feature : ", length2)

with open(output_data, "w") as outfile:
    #jump_index = 0
    for i in range(length):
        #if i % 7 == 0:
            #jump_index = i

        label_temp = label_RGB_list[i].replace("\n", "")
        feature_temp = feature_RGB_list[i].replace("\n", "")

        line = "|labels " + label_temp + " |features " + feature_temp + "\n"
        outfile.write(line)

label_file.close()
feature_file.close()

print("Finish")
