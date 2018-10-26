

label_device = "S8+"
feature_device = "MotoC"
folder_name = "data_2"

base_path = "D:\\Documents\\Thesis\\"
label_data = base_path + label_device + "\\data_set_3\\data_centroid_3.txt"
feature_data = base_path + feature_device + "\\data_set_3\\data_centroid_3.txt"
output_data = base_path + "\\" + folder_name + "\\S8_MotoC_plus_data_7.txt"

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
