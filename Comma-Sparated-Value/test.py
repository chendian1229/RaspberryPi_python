import csv
'''
add_info=['9','10','11','12']

csvFile=open("1.csv","a")

writer=csv.writer(csvFile)

writer.writerow(add_info)
csvFile.close()
'''
with open('1.csv','rb') as csvfile:
    reader=csv.reader(csvfile)
    rows=[row[2] for row in reader]

print(rows)
