import csv
import matplotlib.pyplot as plt
import pystan
import numpy as np

# open the file
with open('assignment7_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    salary=[]
    time=[]
    satisfactory=[]
    i=0
    for row in csv_reader:
        # skip the headers
        if i == 0:
            i += 1
            continue

        # put what we want to keep
        salary.append(float(row[0]))
        time.append(float(row[1]))
        satisfactory.append(float(row[2]))

# convert them as an array
salary=np.asarray(salary)
time=np.asarray(time)
satisfactory=np.asarray(satisfactory)

# make the data
myData={'salary':salary,"time":time,"satisfactory":satisfactory, "N":len(salary)}

# create tha model and train it
sm= pystan.build(file="assignment7.stan")
fit=sm.sampling(data=myData,iter=100,chains=4)

# take the paramenters of the model so we can create it
beta0 = fit['beta0']
beta1 = fit['beta1']
beta2 = fit['beta2']
sigma = fit['sigma']

# plot model
plt.figure(figsize=(8,8))
# for i in np.random.randint(0, len(beta1), 1000):
satisfactory=np.random.normal(beta0[i] + beta1[i] *salary[i] + beta2*time[i],sigma,len(beta1)) 
plt.hist(satisfactory)

# create the plot
plt.show()
    