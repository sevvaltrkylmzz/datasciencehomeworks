# import everything
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(103)
fig, ax = plt.subplots(2,1,figsize=(15,15))

#-------------------------1---------------------------------

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
ax[0].plot(probs,posterior)
ax[0].set_title("Poisson")
ax[0].grid(True)

# --------------------------------------------------------

# crate the probability and a random data
n=18
D = np.random.binomial(100,0.5,n)
# we divide by 100 so we can have float
D =D/100
probs=np.linspace(start=0, stop=1, num=21)

# find the likelihood
likelihood=[]
for x in probs:
    r=[stats.norm.pdf(x,loc=0,scale=r) for r in D ]
    likelihood.append(math.prod(r))
likelihood2=np.asarray(likelihood)

# find the 2 priors
priors1= np.random.uniform(0,1,len(probs))
priors2= np.random.uniform(0,1,len(probs))

# find the 2 diffrent posteriors
posterior1=priors1*likelihood2
posterior2=priors2*likelihood2

# make a 2-dimensional posterior
posterior=np.vstack((posterior1,posterior2))
# because we want to have one dimensional we will find the middle point
# of both posterior so we can depict the posterior with respect to both parameters in a single plot.
finalposterior=np.mean(posterior, axis=0)

# plot the results
ax[1].plot(probs,finalposterior)
ax[1].set_title("Normal")
ax[1].grid(True)

plt.show()