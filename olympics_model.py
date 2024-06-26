# -*- coding: utf-8 -*-
import pandas as pd

teams = pd.read_csv("teams.csv")

teams = teams[["team","country","year","athletes","age","prev_medals","medals"]]

teams

teams.fillna(0, inplace=True)
numeric_columns = ['year', 'athletes', 'age', 'prev_medals', 'medals']
teams[numeric_columns] = teams[numeric_columns].astype(int)

teams

teams.corr()["medals"]

import seaborn as sns

sns.lmplot(x="athletes" , y="medals" , data = teams , fit_reg=True,ci = None)

teams.plot.hist(y="medals")

train = teams[teams["year"] < 2012].copy()
test = teams[teams["year"]  >= 2012].copy()

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

predictors = ["athletes", "prev_medals"]
target = "medals"

reg.fit(train[predictors], train["medals"])

predictions = reg.predict(test[predictors])

import numpy as np

predictions[predictions < 0] = 0
predictions = np.round(predictions)

test["predictions"] = predictions

test

from sklearn.metrics import mean_absolute_error

error = mean_absolute_error(test["medals"], test["predictions"])

errors = (test["medals"] - test["predictions"]).abs()

errors
