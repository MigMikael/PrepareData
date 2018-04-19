"""
1|37,54|3199,27|3206,2276|21,2243
2|43,104|3168,80|3196,2293|24,2293
3|34,81|3177,48|3190,2295|14,2253

"""

# target_device = "iPadMini4"
target_device = "S8+"

dest_path = "C:\\Users\\Mig\\Documents\\Thesis\\" + target_device + "\\data_set_2\\"

with open(dest_path + "coord.txt", 'a') as txtfile:
    for i in range(30):
        line = str(i+1) + "|,|,|,|,"
        if i != 29:
            line += "\n"
        txtfile.write(line)
    print("Finish")
