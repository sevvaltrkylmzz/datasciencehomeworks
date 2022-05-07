# import everything we want
import http.client
import csv
import json

# open a connaction with the api 
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
    'x-rapidapi-key': "3ea296cc0dmsh3edeb64105a11e0p12446fjsna0f3033f3e7b"
    }

# get the information and decode it and turn it to a data which we can change
conn.request("GET", "/api/covid-ovid-data/",headers=headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
theData = json.loads(data)

# open a csv file to export our data
with open('data.csv', 'w', newline='') as csvfile:
    # begin writing the csv file and the first row
    writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Country', 'Max New Cases', 'Date'])
    
    allcountries=[]
    maxNewCases={}
    when={}
    #  for all the data we have
    for eachData in theData:
        country=eachData["Country"]
        # if we have not seen this country
        if country not in allcountries:
            # put the name of the country in the list of the countries
            # and put the first new cases and date we get from this row
            allcountries.append(country)
            maxNewCases[country]=eachData["new_cases"]
            when[country]=eachData["date"]
        else :
            # otherwise we have seen the country and check if 
            # the new data we collected is the data we want
            if maxNewCases[country]<eachData["new_cases"]:
                maxNewCases[country]=eachData["new_cases"]
                when[country]=eachData["date"]
    # for all the countries that we have make a row in our 
    # csv file and export the results
    for country in allcountries:
        writer.writerow([country,maxNewCases[country],when[country]])            
