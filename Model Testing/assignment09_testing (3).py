import pandas as pd
import matplotlib.pyplot as plt
import numpy
import pystan

# Can be exchanged to simple/complex.
df = pd.read_csv("simple.csv")

# Compile simple model
sm = pystan.StanModel(model_code="""
    data{
      int<lower=0> N;
      vector[N] X1;
      vector[N] Y;
    }
    parameters{
      real a;
      real b1;
      real<lower=0> sigma;
    }
    model{
      Y ~ normal(a + b1 * X1 , sigma);
    }
    """)

# Compile complex model:
cm = pystan.StanModel(model_code="""
    data{
      int<lower=0> N;
      vector[N] X1;
      vector[N] X2;
      vector[N] Y;
    }
    parameters{
      real a;
      real b1;
      real b2;
      real<lower=0> sigma;
    }
    model{
      Y ~ normal(a + b1 * X1 + b2 * X2, sigma);
    }
    """)

error_simple = []
error_complex = []

folds = 10

# Folds
for fold in range(0, folds):
    # Splitting data set.
    test = df[(df.index % folds) == fold]
    train = df[(df.index % folds) != fold]

    # Fit the simple model.
    fit = sm.sampling(data={"N": len(train), "Y": train["Y"], "X1": train["X1"]}, iter=4000, chains=1)
    samples = fit.extract()

    # Shame on us not taking the complete posterior.
    a = samples["a"].mean()
    b1 = samples["b1"].mean()

    # Prediction.
    Ypred = a + b1 * test["X1"]

    error_simple.append(sum([pow(x, 2) for x in Ypred - test["Y"]]))

    # Fit the complex model.
    fit = cm.sampling(data={"N": len(train), "Y": train["Y"], "X1": train["X1"], "X2": train["X2"]}, iter=4000, chains=1)
    samples = fit.extract()

    # Shame on us not taking the complete posterior.
    a = samples["a"].mean()
    b1 = samples["b1"].mean()
    b2 = samples["b1"].mean()

    # Prediction.
    Ypred = a + b1 * test["X1"] + b2 * test["X2"]

    error_complex.append(sum([pow(x, 2) for x in Ypred - test["Y"]]))

# What remains to be done is comparing the collected errors
# ...