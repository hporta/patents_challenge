# -*- coding: utf-8 -*-
import xgboost as xgb

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Imputer
import pandas as pd
import numpy as np

# Preprocessing

train_fname = 'train.csv'
test_fname = 'test.csv'
df = pd.read_csv(train_fname, sep=';')
df_test = pd.read_csv(test_fname, sep=';')
train_length = df.shape[0]

#On crée la variable cible

y = df.VARIABLE_CIBLE == 'GRANTED'
encbis = LabelEncoder()
y = encbis.fit_transform(y)
df.drop('VARIABLE_CIBLE',axis=1,inplace=True)

name = ["VOIE_DEPOT","COUNTRY","SOURCE_BEGIN_MONTH","FISRT_APP_COUNTRY","FISRT_APP_TYPE","LANGUAGE_OF_FILLING","FIRST_CLASSE","TECHNOLOGIE_SECTOR",
        "TECHNOLOGIE_FIELD","MAIN_IPC","FISRT_INV_COUNTRY","FISRT_INV_TYPE","SOURCE_IDX_ORI","SOURCE_CITED_AGE","SOURCE_IDX_RAD"]
date = ["PRIORITY_MONTH","FILING_MONTH","PUBLICATION_MONTH",
       "BEGIN_MONTH"]
#On labélise les données catégorielles
       
donnee = pd.concat((df,df_test))
enc = LabelEncoder()
donnee[name] = donnee[name].apply(enc.fit_transform)

#On traite les dates

for i in date:
    donnee[i] = donnee[i].str.extract(r'/([\d]{4})')
    
# On gére les Nan values

imp = Imputer()
donnee  = imp.fit_transform(donnee)

#On split

X_train = donnee[:train_length]
X_test = donnee[train_length:]

#Processing

M_train  = xgb.DMatrix(X_train, label=y)
M_test   = xgb.DMatrix(X_test)
param_xgb   = {'max_depth': 9, 'eta': 0.01,'objective': 'binary:logistic'
, 'subsample': 0.9, 'eval_metric': 'auc','colsample_bytree' :0.7,'seed':27,'nthread':4,'silent': 1,'min_child_weight' : 5}
num_rounds = 2793
booster = xgb.train(param_xgb, M_train, num_rounds)
y_predict  = booster.predict(M_test)
np.savetxt('y_pred.txt', y_predict, fmt='%s')