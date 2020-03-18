
'''
module : getrows.py
version : see module_version variable
Language : Python 3.x
author : andrew christ
email : andrew@openmarmot.com
notes : get rows from a spreadsheet that match a set of keywords in a specified column
'''


#import built in modules
import sys
import csv

#import custom packages

# module specific variables
module_version='0.0' #module software version
module_last_update_date='Feb 25 2020' #date of last update

#global variables


#--------------------------------------------------
def main():
    
    if len(sys.argv) <3:
        print('CLI usage: python3 getrows.py KEY_WORDS_FILE COLUMN_NUMBER SPREADSHEET')
        exit()
    
    keyFile=sys.argv[1]
    columnNum=int(sys.argv[2])
    spreadsheet=sys.argv[3]
    
    #import key words from keyfile into a list
    keywords=returnListFromFile(keyFile)
    
    # check rows against list
    data=getMatchingRows(keywords,spreadsheet,columnNum)
    
    # output results
    writeFile('output.csv',data)
    
#--------------------------------------------------

#--------------------------------------------------
def getMatchingRows(KEYWORDS, SPREADSHEET, COLUMNNUM):
    # if this isn't a list the nested for loop only runs once because the object
    # gets emptied out
    inputfile = list(csv.reader(open(SPREADSHEET, 'r')))
    
    match=[]
    for k in KEYWORDS:
        for row in inputfile:
            if k in row[COLUMNNUM]:
                print(row)
                #for some reason it comes out as a list of lists
                match.append(str(row).replace('[','').replace(']','').replace("'",""))
    return match
#--------------------------------------------------

#--------------------------------------------------
def returnListFromFile(filename):
    list1=[]
    try:
        for line in open(filename):
            line=line.rstrip() #removes whitespace characters
            list1.append(line)
    except FileNotFoundError:
        print('File not found')
        return None
    return list1
#--------------------------------------------------

#--------------------------------------------------
def writeFile(filename,contents):
    fileObj=open(filename,'w') 
    for line in contents:
        fileObj.write(line+'\n') # writes in the line and then adds a new line / drops the cursor
    fileObj.close
#--------------------------------------------------

main()
