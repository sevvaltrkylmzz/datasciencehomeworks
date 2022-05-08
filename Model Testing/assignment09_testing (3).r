library(rstan)

set.seed(1)
N <- 200 # Number of observations.

# Observed variables.
X1 <- rnorm(N) # Normal distributed variable.
X2 <- rnorm(N)  # Normal distributed variable.

# Unobserved variables (later parameters in the model).
a <- 0.5
b1 <- 0.4
b2 <- 0.4 # Effect (or set b2 <- 0 for the simple data set).
sigma <- 0.4

mu <- a + b1 * X1 + b2 * X2 # Linear model

# Observed output variables.
Y <- rnorm(N, mean = mu, sd = sigma) # Output variable.

data <- data.frame(X1 = X1, X2 = X2, Y = Y)
#write.csv(data, "complex.csv", row.names = F)

# CV

error1s <- NULL
error2s <- NULL

for (i in 1:10) {
  # Splitting the data into test and train set.
  test <- (1:200 %% 10) + 1 == i

  Ytest <- Y[test]
  Ytrain <- Y[!test]

  X1test <- X1[test]
  X1train <- X1[!test]

  X2test <- X2[test]
  X2train <- X2[!test]

  model1 <- stan(model_code = "
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
", data = list(X1 = X1train, N = length(X2train), Y = Ytrain), chains = 1)

  model2 <- stan(model_code = "
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
", data = list(X1 = X1train, X2 = X2train, N = length(X2train), Y = Ytrain), chains = 1)

  # Extract samples from the posterior.
  samples1 <- extract(model1)
  samples2 <- extract(model2)

  # We are not using the full posterior (shame on us!!!)
  Ypred1 <- mean(samples1$a) + mean(samples1$b1) * X1test
  Ypred2 <- mean(samples2$a) +
    mean(samples2$b1) * X1test +
    mean(samples2$b2) * X2test

  # Compute sum square error.
  error1 <- sum((Ypred1 - Ytest)^2)
  error2 <- sum((Ypred2 - Ytest)^2)

  error1s <- c(error1s, error1)
  error2s <- c(error2s, error2)
}

#print(mean(error2s - error1s))