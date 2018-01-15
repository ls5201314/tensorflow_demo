import tensorflow as tf
import numpy as np
import csv
import collections

# 线性分类问题
tf.logging.set_verbosity(tf.logging.ERROR)
np.set_printoptions(threshold='nan')
Dataset = collections.namedtuple('Dataset', ['data', 'target'])
file_path = r'C:\Users\ls\Desktop\exam20180111.csv'
def main():
    # Specify that all features have real-value data
    feature_columns = [tf.contrib.layers.real_valued_column("", dimension=4)]

    # Build 3 layer DNN with 10, 20, 10 units respectively.
    classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                                hidden_units=[10, 20, 10],
                                                n_classes=3)
    # Define the training inputs
    def load_csv():
        allElectronicsData = open(file_path, 'rt', encoding='utf8', errors='ignore')
        reader = csv.reader(allElectronicsData)

        data = np.zeros((105, 4), dtype=np.float32)
        target = np.zeros((105,), dtype=np.int)

        for index, row in enumerate(reader):
            if index < 105:
                newRow = [0, 0, 0, 0, 0]
                if row[5] == 'A':
                    newRow[4] = 0
                if row[5] == 'B':
                    newRow[4] = 1
                if row[5] == 'C':
                    newRow[4] = 2
                for i in range(1, 5):
                    newRow[i-1] = row[i]
                target[index] = np.asarray(newRow.pop(-1), dtype=np.int)
                data[index] = np.asarray(newRow, dtype=np.float32)

        return Dataset(data=data, target=target)

    training_set = load_csv()
    def get_train_inputs():
        x = tf.constant(training_set.data)
        y = tf.constant(training_set.target)
        return x, y
    # Fit model.
    classifier.fit(input_fn=get_train_inputs, steps=2000)

    # Classify two new flower samples.
    def predicte_data():
        allElectronicsData = open(file_path, 'rt', encoding='utf8', errors='ignore')
        reader = csv.reader(allElectronicsData)

        newRowList = []
        for index, row in enumerate(reader):
            if index >= 105:
                newRowX = [0, 0, 0, 0]
                for i in range(1, 5):
                    newRowX[i-1] = row[i]
                print("newRowX: " , str(newRowX))
                newRowList.append(newRowX)
        return np.array(newRowList, dtype = np.float32)

    predictions = list(classifier.predict(input_fn=predicte_data))

    print("New Samples, Class Predictions:    {}n".format(predictions))

if __name__ == "__main__":
    main()

exit(0)