import numpy as np
import matplotlib.pyplot as plt

# create subplots
fig, ax = plt.subplots(6,5,figsize=(15,15))
# for our 5 diffrent distribution
for j in range(5): 
    # for our different parameters
    listOfParameters=[(100,100,0), (100,10000,1), (1000,100,2), (1000,10000,3),(10000,100,4), (10000,10000,5)]
    # take parameter 1 and 2 and which place in the graph they are 
    for parameter1,parameter2,i in listOfParameters:
        # we choose the distribution
        # and we take the random numbers from the library numpy
        # and if it is the first time we make this distribution we put at title
        if j==0:
            array = np.random.normal(scale=parameter1,size=parameter2)
            if i==0:
                ax[i,j].set_title("Normal")
        elif j==1:
            array = np.random.exponential(scale=parameter1,size=parameter2)
            if i==0:
                ax[i,j].set_title("Exponential")
        elif j==2:
            array = np.random.binomial(n=parameter1,p=0.5,size=parameter2)
            if i==0:
                ax[i,j].set_title("Binomial")
        elif j==3:
            array = np.random.poisson(lam=parameter1, size=parameter2)
            if i==0:
                ax[i,j].set_title("Poisson")
        else:
            array = np.random.rayleigh(scale=parameter1, size=parameter2)
            if i==0:
                ax[i,j].set_title("Rayleigh")
        # we plot the distribution
        ax[i,j].hist(array,bins=25, density=True, alpha=0.6, color='b')

# show
fig.tight_layout()
plt.show()
