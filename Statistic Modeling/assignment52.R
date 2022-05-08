library(rethinking)

# Simulating data.
set.seed(1)
n <- 4
D <- rnorm(n, mean = 0.5, sd = 0.3)

# Posterior function (taking mu and sigma).
U <- function(mu, sigma) {
  dunif(mu, 0, 1) *
    dunif(sigma, 0, 1) *
    prod(dnorm(D, mu, sigma))
}

# Mu and sigma 'grid'.
mus <- seq(-0, 1, length.out = 100)
sigmas <- seq(0, 1, length.out = 100)
grid <- expand.grid(mu = mus, sigma = sigmas)

# Compute posterior for grid points.
posterior <- sapply(seq_len(nrow(grid)), function(i) U(grid$mu[i], grid$sigma[i]))

# Plot.
contour_xyz(grid$mu, grid$sigma, posterior)