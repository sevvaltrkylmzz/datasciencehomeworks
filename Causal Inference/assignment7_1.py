import csv
import numpy as np
import matplotlib.pyplot as plt

n=1000

salary = np.random.binomial(1,0.5,n)

time=[]

for theSalary in salary:
    if theSalary ==1 :
        prob = 0.9
    else:
        prob = 0.1

    time.append(np.random.binomial(1,prob,1))

time=np.asarray(time)
time=time.flatten()

mu = -0.2 + 0.2*salary - 0.1 *time
sigma = 0.07

satisfactory = np.random.normal(mu,sigma,n)


f = open('data.csv', 'w')

# create the csv writer
writer = csv.writer(f)

writer.writerow(["salary","time","satisfactory"])

# write a row to the csv file
for i in range(n):
    row = [salary[i], time[i], satisfactory[i]] 
    writer.writerow(row)

# close the file
f.close()
