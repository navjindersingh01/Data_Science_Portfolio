import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV

df = pd.read_csv("salary_data_cleaned.csv")
# choose relevent coloumns
columns = ['seniority_level','status','industry','ownership', 'avg_salary', 'python_yn','machine learning_yn', 'sql_yn', 
'r_yn', 'aws_yn', 'deep learning_yn']

df_model = df[columns]
# get dummy data
df_dum = pd.get_dummies(df_model,dtype = int)
# train test split
X = df_dum.drop("avg_salary",axis = 1)
y = df_dum.avg_salary.values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# multiple regeression model
import statsmodels.api as sm

X_sm = sm.add_constant(X)
model = sm.OLS(y,X_sm)

from sklearn.linear_model import LinearRegression, Lasso
lm = LinearRegression()
lm.fit(X_train,y_train)

# print(np.mean(cross_val_score(lm,X_train,y_train,scoring = 'neg_mean_absolute_error',cv = 3)))

# lasso regeression model
lm_l = Lasso(alpha=.01)
lm_l.fit(X_train,y_train)
# print(np.mean(cross_val_score(lm_l,X_train,y_train,scoring = 'neg_mean_absolute_error',cv = 3)))

alpha = []
error = []

# for i in range(1,100):
#     alpha.append(i/100)
#     lml = Lasso(alpha=i/100)
#     error.append(np.mean(cross_val_score(lml,X_train,y_train,scoring = 'neg_mean_absolute_error',cv = 3)))

plt.plot(alpha,error)
# plt.show()

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err,columns=['alpha','error'])
# print(df_err[df_err.error == max(df_err.error)])

# random forest model

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
# print(np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error',cv = 3)))
# tune these models with gridsearch cv

parameters = {'n_estimators':range(10,300,10), 'criterion':('squared_error', 'absolute_error'), 'max_features':('sqrt', 'log2', None)}
gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv = 3)
gs.fit(X_train,y_train)
print(gs.best_score_)
print(gs.best_estimator_)
print(gs.best_params_)

# test ensembles
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error

print(mean_absolute_error(y_test,tpred_lm))
print(mean_absolute_error(y_test,tpred_lml))
print(mean_absolute_error(y_test,tpred_rf))
