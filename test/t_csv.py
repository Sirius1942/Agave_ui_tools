#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
import csv

import csv
filename="segmentation_poc_20181015_sendout_wextra_KC"
def reader():
    rl=[]
    with open('..\data\segmentation_poc_20181015_sendout_wextra_KC.csv') as f:
        f_csv = csv.reader(f)
        headerline=next(f_csv)
        rl.append(headerline)

        lines=[]
        for row in f_csv:
            #print(row)
            new_row={}
            for num in range(0,len(row)):
                new_row[headerline[num]]=row[num]
            lines.append(new_row)
        #print(lines)
        #rl[0]=headers
        rl.append(lines)
        return rl

def writer(rows,filename):

    statnum=0
    endnum=statnum+1000

    tolnum=len(rows[1])



    while endnum<tolnum:
        newlines=[]
        for rownum in range(statnum,endnum):
            linetext=rows[1][rownum]
            newlines.append(linetext)
        #print(newlines)
        cvswriter(newlines,filename+"_"+str(statnum)+"_"+str(endnum),rows[0])
        statnum=endnum
        endnum+=1000

    if endnum>tolnum:
        newlines = []
        for rownum in range(statnum, tolnum):
            linetext = rows[1][rownum]
            newlines.append(linetext)
        cvswriter(newlines, filename + "_" + str(statnum) + "_" + str(tolnum),rows[0])

def cvswriter(rows,filename,headers):
    # print(headers)
    # print(rows)
    with open('..\\result\\'+filename+'.csv', 'w', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

if __name__ == '__main__':
    rows=reader()
    writer(rows,filename)



