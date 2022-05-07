import csv
import matplotlib.pyplot as plt
import stan
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
sm= stan.build(file="assignment6_2.stan")
fit=sm.sampling(data=myData,iter=100,chains=4)

# take the paramenters of the model so we can create it
alpha = fit['alpha']
beta = fit['beta']
sigma = fit['sigma']

# plot model
plt.figure(figsize=(8,8))
for i in range(0, len(alpha)):
    plt.scatter(age, alpha[i] + beta[i] * age)

# create the plot
plt.show()

    