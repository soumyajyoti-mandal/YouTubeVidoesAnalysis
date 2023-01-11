import csv
import glob
import os
import json
#finding all csv files
list_csv  = glob.glob(r"archive\*.csv")
#finding all json files
list_json =  glob.glob(r"archive\*.json")

totalrecords =[]
for csvfile in list_csv:
    for jsonfile in list_json:
        #matching csv file to json file to map category id from csv to title in json file
        if os.path.basename(csvfile)[0:2] == os.path.basename(jsonfile)[0:2]:
            samplecsvfile = open(csvfile,"r",errors="ignore")
            csvreader = csv.reader(samplecsvfile)
            sampledata = list(csvreader)
            samplecsvfile.close()
            f = open(jsonfile)
            data = json.load(f)
            for q in range(1,len(sampledata)):
                sampledata[q].insert(0,os.path.basename(csvfile)[0:2])
                for w in data["items"]:
                    if sampledata[q][5]== w.get("id"):
                        sampledata[q].insert(6,w.get("snippet").get("title"))
            f.close()
            #consolidating data from all csv files to one list
            totalrecords.append(sampledata)
totalrecords[0][0].insert(0,"region")
#adding column category beside category_id
totalrecords[0][0].insert(6,"category")

#removing header record of each csv file from the list
for e in range(1,len(totalrecords)):
    totalrecords[e].pop(0)

outputfile=open("output.csv","w",newline='')
outputwriter = csv.writer(outputfile)
for v in range(len(totalrecords)):
    for x in range(len(totalrecords[v])):
        outputwriter.writerow(totalrecords[v][x])

outputfile.close()