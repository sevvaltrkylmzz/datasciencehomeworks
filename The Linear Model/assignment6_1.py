import csv
import matplotlib.pyplot as plt

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

# create the plot
plt.figure(figsize=(8,8))
plt.scatter(age,height)
plt.xlabel('heights')
plt.title('Data3: Heights')
plt.ylabel('how many people have that height')
plt.show()