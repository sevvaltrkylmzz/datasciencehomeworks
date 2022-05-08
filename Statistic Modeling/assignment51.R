# Simulated data.
set.seed(1)
n <- 9
D <- rpois(n, lambda = 0.7)

# The lambda 'grid'.
lambdas <- seq(0, 4, length.out = 101)

# Producing the posterior, i.e., that lambda has produced this data.
posterior <- sapply(lambdas, function(lambda) {
  prod(dpois(D, lambda)) * dunif(lambda, 0, 4)
})

plot(lambdas, posterior, type = "l")