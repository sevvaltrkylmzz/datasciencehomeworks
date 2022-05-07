import csv
text = [{"id":"45ce8f66-c6a0-45ab-9d9c-3061f59187e7","symbol":"AFG","Country":"Afghanistan","Continent":"Asia","date":"2020-05-22","total_cases":8676,"new_cases":531,"total_deaths":193,"new_deaths":6,"total_tests":0,"new_tests":0},{"id":"7f2e5620-2c92-4420-ae1a-d6c1f913945a","symbol":"AFG","Country":"Afghanistan","Continent":"Asia","date":"2020-05-23","total_cases":9216,"new_cases":540,"total_deaths":205,"new_deaths":12,"total_tests":0,"new_tests":0},{"id":"5ed2b29b-f9d6-4ad8-b4db-f2192fd9491a","symbol":"AFG","Country":"Afghanistan","Continent":"Asia","date":"2020-05-24","total_cases":9998,"new_cases":782,"total_deaths":216,"new_deaths":11,"total_tests":0,"new_tests":0}]
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(['Country', 'Max New Cases', 'Date'])
    allcountries=[]
    maxNewCases={}
    when={}
    for eachData in text:
        country=eachData["Country"]
        if country not in allcountries:
            allcountries.append(country)
            maxNewCases[country]=eachData["new_cases"]
            when[country]=eachData["date"]
        else :
            if maxNewCases[country]<eachData["new_cases"]:
                maxNewCases[country]=eachData["new_cases"]
                when[country]=eachData["date"]
    for country in allcountries:
        writer.writerow([country,maxNewCases[country],when[country]])