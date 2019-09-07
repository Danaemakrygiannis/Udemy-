import csv
import os

udemy_csv = os.path.join (".","resources","web_starter.csv")

title= []
price= []
subscribers= []
reviews= []
reviews_percent= []
length=[]


with open (udemy_csv, "r", encoding= "UTF-8") as csvfile:
    csvreader = csv.reader (csvfile, delimiter=",")

    test= next (csvreader)
    
    for row in csvreader:
        #add title
        title.append(row[1])
        #add price 
        price.append(row[4])
        #add subscribers
        subscribers.append(row[5])
        #revires
        reviews.append (row[6])
        #percent of reviews
        percent = round (int(row[6])/int (row[5]),2)
        reviews_percent.append(percent)
        #length
        new_length= row[9].split(" ")
        length.append(float(new_length[0]))
print(length)

cleanCsv = zip(title, price, subscribers, reviews, reviews_percent, length)

outputFile= os.path.join("webFinal.csv")

with open(outputFile, "w", newline="") as datafile:
    writer= csv.writer(datafile)
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews", "Percent of Reviews", "Length of Course"])
    writer.writerows(cleanCsv)
