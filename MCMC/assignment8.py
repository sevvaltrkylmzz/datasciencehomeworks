# import everything
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(103)
fig, ax = plt.subplots(2,1,figsize=(15,15))

# crate the probability and a random data
n=18
D = np.random.binomial(2,0.5,n) # we have put 2 as the pdf reaches until 2
probs=np.linspace(start=0, stop=1, num=21)

# find the likelihood
likelihood=[]
for x in probs:
    r=[stats.poisson.pmf(x,r) for r in D ]
    likelihood.append(math.prod(r))
likelihood2=np.asarray(likelihood)

# find the priors
priors= np.random.uniform(0,4,len(probs))

# find the posterior
posterior=priors*likelihood2

# plot the results
ax[0].hist(posterior)
ax[0].set_title("Poisson")
ax[0].grid(True)

#---------------------------------







plt.show()
