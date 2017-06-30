
import csv
with open('5组电设器件清单.csv') as f:
    f_csv=csv.reader(f)
    headers=next(f_csv)
    for row in f_csv:
        print(row)
'''
from collections import namedtuple
import csv
with open('1.csv') as f:
    f_csv=csv.reader(f)
    headings=next(f_csv)
    Row=namedtuple('Row',headings)
    for r in f_csv:
        row=Row(*r)
'''

def deal_value(read_csv):
    
    try:
        f_write=open('2.csv','a')
        f_write_csv=csv.writer(f_write)
        s=[x*x for x in range(5)]
        print(s)
        for row in read_csv:
            #print(row)
            f_write_csv.writerow(row)
    except ValueError:
        
        print("We meet some value_error")
    
def main():
    with open('5组电设器件清单.csv','r') as f_read:
        f_read_csv=csv.reader(f_read)
        headers=next(f_read_csv)
        deal_value(f_read_csv)


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
        
