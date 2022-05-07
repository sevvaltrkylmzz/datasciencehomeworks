import matplotlib.pyplot as plt
import csv

  
with open('Assignment3\data2.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    i=0
    flag1=False
    flag2=False
    for row in lines:
        # to skip the headers
        if i == 0:
            i += 1
            continue
        # decide which color to make it
        if row[2]=='west':
            # if it is the first time seeing a west, label it
            # otherwise just put it into the plot
            # we do this so we label only one time 
            if flag1 is False:
                plt.scatter(float(row[0]),float(row[1]),color='g',label="west")
                flag1= True
            else:
                plt.scatter(float(row[0]),float(row[1]),color='g')

        elif row[2]=='east':
            # if it is the first time seeing a east, label it
            # otherwise just put it into the plot
            # we do this so we label only one time 
            if flag2 is False:
                plt.scatter(float(row[0]),float(row[1]),color='r',label="east")
                flag2= True
            else:
                plt.scatter(float(row[0]),float(row[1]),color='r')


    # create the plot
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.title('Data2: Salary')
    plt.grid()
    plt.legend()
    plt.show()