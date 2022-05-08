# S -> H, S -> T, T -> H
set.seed(1)
library(rstan)

N <- 500

S <- rnorm(N)
T <- rnorm(N, mean = -S)
H <- rnorm(N, mean = (0 + 1 * S + -1 * T), sd = 1)

# print(round(data.frame(S = S, T = T, H = H),2))

model <- stan(model_code = "
data{
  int<lower=0> N;
  vector[N] S;
  vector[N] T;
  vector[N] H;
}
parameters{
  real<lower=0> sigma;
  real a;
  real bS;
  real bT;
}
model{
  vector[N] mu;
  mu = a + bS * S + bT * T;
  H ~ normal(mu, sigma);
}
", data = list(N = N, S = S, T = T, H = H))
samples <- extract(model)

hist(samples$bS)
# ...