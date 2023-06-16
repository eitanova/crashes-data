import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split ,GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn import metrics


# Delete all the line with Nan values and not relevant values
def clean_data(gov_data):
    gov_data = gov_data[gov_data['year'].apply(lambda x: len(str(x)) == 4)]
    gov_data = gov_data.dropna(subset=['year'])
    gov_data = gov_data.dropna(subset=['month'])
    gov_data = gov_data.dropna(subset=['accident_severity'])
    return gov_data


# use LogisticRegression to apply LogisticRegression on the data
def apply_LogisticRegression(gov_data,x_list, y_list):
    gov_data.fillna(0)
    logisticreg = LogisticRegression(max_iter=65000)

    X = gov_data[x_list]
    y = gov_data['accident_severity']
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=43)
    logisticreg.fit(x_train, y_train)
    y_pred = logisticreg.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy ,y_test, y_pred


# build confusion matrix on the resukts from the LogisticRegression
def build_confusion_matrix(y_test, y_pred):
    cm = metrics.confusion_matrix(y_test, y_pred)
    cm_df = pd.DataFrame(cm)
    return cm_df

def convert_to_numerical(gov_data):
    mapping = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6 ,'7': 7 ,'8': 8 ,'9': 9 ,'0': 0 ,'2018': 2018 ,'2019': 2019 }
    gov_data = gov_data.replace(mapping)
    return gov_data


if __name__ == '__main__':
    gov_data = pd.read_csv("C:\\Users\\2eita\\Desktop\\b.csv")

    gov_data = clean_data(gov_data)
    x_list_lr = ['year', 'month', 'weather', 'day_type', 'day_time', 'day']
    y_list_lr = ['accident_severity']
    accuracy, y_test, y_pred = apply_LogisticRegression(gov_data, x_list_lr, y_list_lr)
    cm_df = build_confusion_matrix(y_test, y_pred)
    print(cm_df)
    print(accuracy)

