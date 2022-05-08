shapes <- c(1, 4, 10, 100)
ns <- c(1, 10, 100, 1000, 10000)
#pdf(file = "plot.pdf", width = 10, height = 10)

par(mfcol = c(length(ns), length(shapes)), mar = c(2, 4, 2, 0))

for (shape in shapes) {
  for (n in ns) {
    data <- rgamma(n, shape)
    hist(data,
         xlab = "",
         main = paste0("n=", n, " and shape=", shape))
  }
}
#dev.off()