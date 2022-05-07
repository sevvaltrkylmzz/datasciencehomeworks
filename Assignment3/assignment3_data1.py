import csv
import matplotlib.pyplot as plt

with open('Assignment3\data1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ourData={}
    count=-1
    for row in csv_reader:
        count+=1
        # to avoid the headlines
        if count == 0 :
            continue
        # if we have not seen the country
        if row[0] not in ourData:
            ourData[row[0]]=1
        else:
        # We have seen the country
            ourData[row[0]]+=1

    # make everything a percentage
    for i in ourData.keys():
        ourData[i]=round((ourData[i]/count)*100,2)
 
    # put the data into the graph
    fig, ax=plt.subplots(figsize=(15,15))
    graph=ax.bar(ourData.keys(),ourData.values())
    
    # rotate the labels and make the title
    ax.set_xticklabels(ourData.keys(), rotation=45)
    ax.set_title('Data 1: Religions in Germany')

    # put the percentage 
    i = 0
    for p in graph:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        ax.text(x+width/2,
                y+height*1.01,
                str( ourData[list(ourData.keys())[i]])+'%',
                ha='center',
                weight='bold')
        i+=1
    
    plt.show()
    
