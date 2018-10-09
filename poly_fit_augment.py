from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import numpy


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
    with open(test_path, "r") as test_file:
        for line in test_file:
            label, feature = line.split("|features ")

            f_r, f_g, f_b = feature.split(" ")
            predict.append([int(f_r), int(f_g), int(f_b)])

    return predict


train_path = "D:\\Documents\\Thesis\\S8_MotoC\\S8_MotoC_plus_train_data_5.txt"
test_path = "D:\\Documents\\Thesis\\S8_MotoC\\S8_MotoC_plus_test_data_5.txt"

input_X, vector = loadTrainData(train_path)
poly = PolynomialFeatures(degree=3)

X_ = poly.fit_transform(input_X)
input_X = None
X_ = numpy.delete(X_, (0), axis=1)

clf = linear_model.LinearRegression()
clf.fit(X_, vector)
X_, vector = None, None

predict = loadTestData(test_path)
predict_ = poly.fit_transform(predict)
predict_ = numpy.delete(predict_, (0), axis=1)
predicted = clf.predict(predict_)

print(predicted[:5])
