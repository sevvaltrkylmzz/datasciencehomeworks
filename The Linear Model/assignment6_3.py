import csv
import matplotlib.pyplot as plt
import pystan
import numpy as np
# open the file
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    age=[]
    height=[]
    i=0
    for row in csv_reader:
        # skip the headers
        if i == 0:
            i += 1
            continue

        # put what we want to keep
        height.append(float(row[0]))
        age.append(float(row[2]))

# convert them as an array
age=np.asarray(age)
height=np.asarray(height)

# make the data
myData={'x':age,"y":height, "N":len(age)}

# create tha model and train it
sm= pystan.StanModel(file="assignment6_3.stan")
fit=sm.sampling(data=myData,iter=100,chains=4)

# take the paramenters of the model so we can create it
beta1 = fit['beta1']
beta2 = fit['beta2']
beta3 = fit['beta3']
sigma = fit['sigma']

# plot model
plt.figure(figsize=(8,8))
for i in np.random.randint(0, len(beta1), 1000):
    plt.scatter(age, beta1[i] + beta2[i] * age + beta3[i]*age*age)

# create the plot
plt.show()