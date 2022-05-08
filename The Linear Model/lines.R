# Loading library and data set.
library(rethinking)
library(rstan)

data(Howell1)
df <- Howell1

# The mean age (later used to center age at a mean of 0).
age_bar <- mean(df$age)

model <- stan(model_code = "
data{
  int<lower=0> N;
  real age_bar;
  vector[N] age;
  vector[N] h;
}

parameters{
  real a;
  real b;
  real <lower=0, upper=50> sigma;
}

model{
  sigma ~ uniform(0, 50);
  a ~ normal(178, 10);
  b ~ normal(0, 10);
  h ~ normal(a + b * (age - age_bar), sigma);
}"
  , data = list(h = df$height, age = df$age, age_bar = age_bar, N = length(df$age)), chains = 1)

samples <- extract.samples(model)

# Plotting the points.
plot(df$age, df$height, ylim = c(60, 200))

# Plotting the regression lines.
ages <- seq(0, 100, length.out = 60)
for (i in 1:100) {
  mu <- samples$a[i] + samples$b[i] * (ages - age_bar)
  lines(ages, mu, col = rgb(0, 1, 0, 0.2))
}
