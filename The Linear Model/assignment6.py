import csv
import matplotlib.pyplot as plt

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ourData={}
    i=0
    for row in csv_reader:
        # skip the headers
        if i == 0:
            i += 1
            continue
        # make the height to number and not a string
        number=float(row[0])
        # add it to our data if there isn't already
        # otherwise increase the time we have seen it
        if number not in ourData.keys():
            ourData[number] = 1
        else:
            ourData[number] +=1

    # create the plot
    plt.figure(figsize=(8,8))
    plt.scatter(ourData.keys(), ourData.values())
    plt.xlabel('heights')
    plt.title('Data3: Heights')
    plt.ylabel('how many people have that height')
    plt.show()