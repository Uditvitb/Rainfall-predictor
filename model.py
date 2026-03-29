import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def prediction(ml,l):
    return ml.predict(l)

df=pd.read_csv("Rainfall.csv")
df=df.drop(columns=["day","dewpoint"])

df.rename(columns={
    "         winddirection":"wind_direction",
    "pressure ":"pressure",
    "humidity ":"humidity",
    "cloud ":"cloud"
},inplace=True)

df["rainfall"]=df["rainfall"].map({"yes":1,"no":0})

X=df.drop(columns="rainfall")
Y=df["rainfall"]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

ml=DecisionTreeClassifier()
ml.fit(X_train,Y_train)

Y_Predict=ml.predict(X_test)

accuracy=accuracy_score(Y_test,Y_Predict)