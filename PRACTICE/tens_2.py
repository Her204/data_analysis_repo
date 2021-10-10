import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.layers as layers

df = pd.read_csv("/mnt/c/users/user/onedrive/escritorio/sales_data.csv")

lst = []
for col in df.columns:
    if df[col].dtype == "object" and col != "Date":
        values = df[col].unique()
        lst.append(col)
        for enum,val in enumerate(values):
            if col=="Customer_Gender":
                df[col] = df[col].replace(val,enum)
            df[col] = df[col].replace(val,np.random.randn(1)[0])

df_int = df.copy()

for col in df_int.columns:
    if len(df[col].unique()) == 2:
        goal_col = col

print(df.columns)
df_int = df_int.drop(columns=lst,axis=1)
print(df_int.columns)
X_train = df_int[df_int.columns[1:]][:int(len(df_int)*0.7)]
y_train = df[goal_col][:int(len(df_int)*0.7)]
X_valid = df_int[df_int.columns[1:]][int(len(df_int)*0.7):]
y_valid = df[goal_col][int(len(df_int)*0.7):]

print(X_train.shape,y_train.shape,X_valid.shape,y_valid.shape)

X_train = (X_train - X_train.min())/(X_train.max()-X_train.min())
y_train = (y_train - y_train.min())/(y_train.max()-y_train.min())
X_valid = (X_valid - X_valid.min())/(X_valid.max()-X_valid.min())
y_valid = (y_valid - y_valid.min())/(y_valid.max()-y_valid.min())

X_train = X_train.values
y_train = y_train.values
X_valid = X_valid.values
y_valid = y_valid.values

model = keras.Sequential([
             layers.Dense(30,activation="relu",input_shape=[9]),
             layers.Dropout(.2),
             layers.Dense(15,activation="relu"),
             layers.Dropout(.2),
             layers.Dense(5,activation="relu"),
             layers.Dropout(.2),
             layers.Dense(1,activation="sigmoid")])

model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=["binary_accuracy"])
history = model.fit(X_train,y_train,
                    epochs=10,batch_size=10,
                    validation_data=(X_valid,y_valid))

print(model.predict(X_valid))
