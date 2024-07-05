import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

subfolder = 'model_training'
original_directory = os.getcwd()
new_directory = os.path.join(original_directory, subfolder)
os.chdir(new_directory)
print(os.getcwd())
data_read = os.path.join('..', 'data_extract_from_s3', 'healthcare_dataset.csv')
df=pd.read_csv(data_read)



df.drop(["Name", "Doctor", "Hospital", "Room Number","Insurance Provider", "Date of Admission","Discharge Date"], axis = 1, inplace = True)
df['Billing Amount'] = df['Billing Amount'].round(-3)

le = LabelEncoder()
cat_cols = []
for col in df.columns:
    if df[col].dtypes == "object":
        cat_cols.append(col)
for col in cat_cols:
    df[col] = le.fit_transform(df[col])
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
# from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)



# from sklearn.model_selection import train_test_split


y_pred = rfc.predict(X_test)
print("Validation Accuracy", accuracy_score(y_test, y_pred))

pickle_out = open("classifier.pkl","wb")
pickle.dump(rfc, pickle_out)
pickle_out.close()