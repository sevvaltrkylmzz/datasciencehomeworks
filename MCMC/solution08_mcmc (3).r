# Simulated data.
set.seed(1)
n <- 9
D <- rpois(n, lambda = 0.7)

# The lambda 'grid'.
lambdas <- seq(0, 4, length.out = 101)

U <- function(lambda) {
  prod(dpois(D, lambda)) * dunif(lambda, 0, 4)
}

# Grid approx of posterior.
# Producing the posterior, i.e., that lambda has produced this data.
posterior <- sapply(lambdas, function(lambda) {
  U(lambda)
})


# Metropolis Hastings
# Start with random point.
x <- 1
samples <- NULL

for (i in 1:20000) {
  next_x <- rnorm(1, mean = x, sd = 0.1)

  if (next_x > 0 && runif(1,0,1) < U(next_x) / U(x)) {
    # Accept.
    x <- next_x
    samples <- c(samples, x)
  }
}
hist(samples, breaks = 40, freq = F)
lines(lambdas, posterior / max(posterior), lwd = 2)
