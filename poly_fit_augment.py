from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import numpy
import math


train_path = "D:\\Documents\\Thesis\\data\\MotoC_iPad_plus_train_data_5.txt"
test_path = "D:\\Documents\\Thesis\\data\\Random\\MotoC_iPad_random_test_5.txt"
# len_data = 1525500
# len_data = 67500
# len_data = 11200
len_data = 548800


def loadTrainData(data_path):
    input_X = []
    vector = []
    with open(data_path, "r") as data_file:
        for line in data_file:
            label, feature = line.split("|features ")
            label = label.replace("|labels ", "")

            f_r, f_g, f_b = feature.split(" ")
            input_X.append([int(f_r), int(f_g), int(f_b)])

            l_r, l_g, l_b, sp = label.split(" ")
            vector.append([int(l_r), int(l_g), int(l_b)])
    return input_X, vector


def loadTestData(test_path):
    predict = []
    ground_truth = []
    with open(test_path, "r") as test_file:
        for line in test_file:
            label, feature = line.split("|features ")
            label = label.replace("|labels ", "")

            f_r, f_g, f_b = feature.split(" ")
            predict.append([int(f_r), int(f_g), int(f_b)])

            l_r, l_g, l_b, sp = label.split(" ")
            ground_truth.append([int(l_r), int(l_g), int(l_b), ])
    return predict, ground_truth


input_X, vector = loadTrainData(train_path)
poly = PolynomialFeatures(degree=3)

X_ = poly.fit_transform(input_X)
X_ = numpy.delete(X_, (0), axis=1)

clf = linear_model.LinearRegression()
clf.fit(X_, vector)

predict, ground_truth = loadTestData(test_path)
predict_ = poly.fit_transform(predict)
predict_ = numpy.delete(predict_, (0), axis=1)
predicted = clf.predict(predict_)
predicted = [[int(round(x[0])), int(round(x[1])), int(round(x[2]))] for x in predicted]

print(predict[:5])
print(predicted[:5])
print(ground_truth[:5])

sum_D_label_linear = 0
sum_diff_label_linear_r = 0
sum_diff_label_linear_g = 0
sum_diff_label_linear_b = 0
for i in range(len_data):
    sum_D_label_linear += math.sqrt(
        (ground_truth[i][0] - predicted[i][0]) ** 2 + (ground_truth[i][1] - predicted[i][1]) ** 2 + (
                ground_truth[i][2] - predicted[i][2]) ** 2)
    sum_diff_label_linear_r += abs(ground_truth[i][0] - predicted[i][0])
    sum_diff_label_linear_g += abs(ground_truth[i][1] - predicted[i][1])
    sum_diff_label_linear_b += abs(ground_truth[i][2] - predicted[i][2])

avg_D_label_linear = sum_D_label_linear / len_data
avg_diff_r = sum_diff_label_linear_r / len_data
avg_diff_g = sum_diff_label_linear_g / len_data
avg_diff_b = sum_diff_label_linear_b / len_data
print("Average Distance Diff : ", avg_D_label_linear)
print("Average R Diff : ", avg_diff_r)
print("Average G Diff : ", avg_diff_g)
print("Average B Diff : ", avg_diff_b)