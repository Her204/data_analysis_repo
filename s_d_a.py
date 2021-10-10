import pandas as pd 
import datetime
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
#from sklearn.preprocessing import Imputer
from sklearn.model_selection import GridSearchCV
import lightgbm as lgb
from lightgbm import LGBMRegressor 
import numpy as np

df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df.Date)
df = df.drop(["Month","Day","Year"],axis=1)

y = df.Profit
X = df.drop("Profit",axis=1)

num_cols = [col for col in X.columns if "int" in str(X[col].dtype) or
            "flo" in str(df[col].dtype) ]
cat_cols = [col for col in X.columns if "ob" in str(X[col].dtype)]

X_train,X_val,y_train,y_val= train_test_split(X,y,
                    train_size=0.6,test_size=0.4,random_state=0)

cols = cat_cols+num_cols

X_train = X_train[cols]
X_val = X_val[cols]

numerical_transformer = SimpleImputer(strategy="constant")
categorical_transformer = Pipeline(steps=[
    ("imputer",SimpleImputer(strategy="most_frequent")),
    ("onehot",OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[("num",numerical_transformer,num_cols),
                ("cat",categorical_transformer,cat_cols)
])

#model = ensemble.RandomForestRegressor(n_estimators=10,
#                                        random_state=0)
d_train = lgb.Dataset(X_train,label=y_train)
lgbm_hparams = {
    #"learning_rate":np.array([0.05]),
    #"boosting_type":["dart"],
    #"objective":["regression"],
    #"metric":["mae"],
    #"num_leaves":[100],
    #"max_depth":[10]
    "imp__strategy":["mean","median","most_frequent"],
    "feat_select__k":[5,10]
}

my_pipeline = Pipeline(steps=[("preprocessor",preprocessor),
                        ("feat_select",SelectKBest()),
                        ("imp",SimpleImputer(missing_values="NaN")),
                        ("model",LGBMRegressor())])

cv = GridSearchCV(my_pipeline,lgbm_hparams,
                  scoring="neg_mean_absolute_error")
cv.fit(X_train,y_train)

preds = cv.predict(X_val)

print(preds)





