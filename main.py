from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

def dataProcessAuto():
    f_test = open("Testing.txt", "r")
    f_train = open("Training.txt", "r")
    lines_test = f_test.readlines()
    lines_train = f_train.readlines()
    resultTrainX = []
    resultTrainY = []
    resultTestX = []
    resultTestY = []
    for i in lines_train[0:10501]:
        temp = i.rstrip()
        temp = temp.split(",")
        resultTrainX.append(temp[0:6])
        resultTrainY.append(temp[6])
    for i in lines_test[0:100]:
        temp = i.rstrip()
        temp = temp.split(',')
        resultTestX.append(temp[0:6])
        resultTestY.append(temp[6])
    return resultTrainX, resultTrainY, resultTestX, resultTestY

def run():
    # Pull data
    dataPointsTrainX, dataPointsTrainY, dataPointsTestX, dataPointsTestY = dataProcessAuto()

    #svclassifier = SVC(kernel='poly',degree=4)
    #print("For Polynomial 4 Degrees")
    #svclassifier = SVC(kernel='poly', degree=2)
    #print("For Polynomial 2 Degrees")

    svclassifier = SVC(kernel='linear')
    print("For Linear")


    svclassifier.fit(dataPointsTrainX, dataPointsTrainY)
    y_pred = svclassifier.predict(dataPointsTestX)

    print(confusion_matrix(dataPointsTestY, y_pred))
    print(classification_report(dataPointsTestY, y_pred))

if __name__ == "__main__":
    run()