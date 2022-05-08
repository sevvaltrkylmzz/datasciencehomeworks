# Loading library and data set.
library(rethinking)
library(rstan)

data(Howell1)
df <- Howell1

age_bar <- mean(df$age)

model <- stan(model_code = "
data{
  int<lower=0> N;
  vector[N] age;
  vector[N] h;
}

parameters{
  real a;
  real b1;
  real b2;
  real <lower=0, upper=50> sigma;
}

model{
  vector[N] mu;
  sigma ~ uniform(0, 50);
  b1 ~ normal(0, 10);
  b2 ~ normal(0, 10);
  for(n in 1:N){
    mu[n] = a + b1 * age[n] + b2 * age[n]^2;
  }
  h ~ normal(mu, sigma);
}"
  , data = list(h = df$height, age = df$age, N = length(df$age)), chains = 1)

samples <- extract.samples(model)

# Plotting the points.
plot(df$age, df$height, ylim = c(-20, 200))

# Plotting the regression lines.
ages <- seq(0, 100, length.out = 60)

for (i in 1:100) {
  mu <- samples$a[i] + samples$b1[i] * ages + samples$b2[i] * ages^2
  lines(ages, mu, col = rgb(1, 0, 0, 0.2))
}
