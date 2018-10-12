source_file = "D:\\Documents\\Thesis\\data\\S8_MotoC_plus_test_data_5.txt"
dest_file = "D:\\Documents\\Thesis\\data\\MotoC_S8_plus_test_data_5.txt"

data_list = []

with open(source_file, "r") as file:
    for line in file:
        data_list.append(line)

print(len(data_list))

count = 0
with open(dest_file, "w") as file:
    for item in data_list:
        piece = item.split(" ")
        piece[7] = piece[7].replace("\n", "")

        line = piece[0] + " " + piece[5] + " " + piece[6] + " " + piece[7] + " " + piece[4] \
               + " " + piece[1] + " " + piece[2] + " " + piece[3] + "\n"
        file.write(line)
        count += 1

print(count)
print("Finish")

