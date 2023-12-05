import tkinter as tk
import PyPDF2
import pandas as pd
import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()
root.geometry('+%d+%d'%(450,10))
root.title('Result Analysis')
root.iconbitmap('download.ico')

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# logopython
logo = ImageTk.PhotoImage(Image.open('download.png'))
logo_label = tk.Label(image=logo, bg="#ffffff")
logo_label.image = logo
logo_label.grid(column=1, row=0, pady=10)  # Added pady parameter for padding

mcadeptname = tk.Label(root, text="MCA Department", font="Raleway")
mcadeptname.grid(columnspan=3, column=0, row=1, pady=10)  # Added pady parameter for padding

# instructions
instructions = tk.Label(root, text="Select a PDF file to analyze the data", font="Raleway")
instructions.grid(columnspan=3, column=0, row=2, pady=10)  # Added pady parameter for padding
def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def intializeAll(givenStudentList):
    rollNo = ['rollNo', givenStudentList[0]]
    name = ['name']
    t = 1
    n = ""
    while(len(givenStudentList[t+1])!=1 or  not(givenStudentList[t+1]!='M' or givenStudentList[t+1]!='F')):
        n = n + " " +givenStudentList[t] 
        t = t+1
    name.append(n)
    motherName = ['Mother_Name', givenStudentList[t]]
    gender = ['Gender', givenStudentList[t+1]]
    #logic for Grade Points 
    if 'POINTS:' in givenStudentList:
        index = givenStudentList.index('POINTS:')
        points = ['GradePoints', givenStudentList[index+1]]
        index = givenStudentList.index('CREDITS')
        credits = ['TotalCredits', givenStudentList[index+1]]
        index = givenStudentList.index('SGPA')
        temp = []
        index = index + 1
        d = 1
        while(givenStudentList[index]!='TOTAL'):
            if is_float(givenStudentList[index][0:5]) and d<=semester:
                temp.append(['Sem'+str(d), givenStudentList[index][0:5]])
                d = d+1
            index = index+1
    else:
        points = ['GradePoints', '0']
        credits = ['TotalCredits', '0']
        d = 1
        temp=[] 
        while(d<=semester):
            temp.append(['Sem'+str(d), '0'])
            d=d+1
    
    global subjectsAvailable
    subjectsAvailable = []
    for i in givenStudentList:
        if (len(i)==6 and i.isnumeric()) or (len(i)==7 and i[0:6].isnumeric()):
            subjectsAvailable.append(i)
    lastSubject = subjectsAvailable[-1]
    length = len(givenStudentList)
    i = 0
    nMarks = [] 
    try:
        while(givenStudentList[i]!=lastSubject):
            demoMarks = []
            if (len(givenStudentList[i])==6 and givenStudentList[i].isnumeric()) or (len(givenStudentList[i])==7 and givenStudentList[i][0:6].isnumeric()):
                if len(givenStudentList[i])==7 and givenStudentList[i][0:6].isnumeric():
                    demoMarks.append(givenStudentList[i][0:6])
                else:
                    demoMarks.append(givenStudentList[i])
                i=i+1
                while(givenStudentList[i] not in subjectsAvailable):
                    demoMarks.append(givenStudentList[i])
                    i=i+1
            else:
                i=i+1
            nMarks.append(demoMarks)
        demoMarks=[]
        demoMarks.append(givenStudentList[i])
        demoMarks.append(givenStudentList[i+1])
        demoMarks.append(givenStudentList[i+2])
        demoMarks.append(givenStudentList[i+3])
        demoMarks.append(givenStudentList[i+4])
        demoMarks.append(givenStudentList[i+5])
        nMarks.append(demoMarks)
    except:
        pass
    
    lastMarks=[]
    for i in nMarks:
        if(len(i)==0):
            pass
        else:
            lastMarks.append(i)

    nMarks=[]
    details=[]
    details.append(rollNo)
    details.append(name)
    details.append(motherName)
    details.append(gender)
    details.append(points)
    details.append(credits)
    for i in temp:
        details.append(i)
    
    for i in lastMarks:
        if 'GRADE' in i:
            pass
        else:
            nMarks.append(i)
            
    for i in nMarks:
        demo = i
        for j in range(len(i)):
            if '*' in i[j]:
                demo2 = i[j].split('*')
                i.remove(i[j])
                i.insert(j,demo2[0])
                i.insert(j+1,'0')
            if '$' in i[j]:
                demo2 = i[j].split('$')
                i.remove(i[j])
                i.insert(j,demo2[0])
                i.insert(j+1,'0')
        
    fullDetails = []
    fullDetails.append(details)
    fullDetails.append(nMarks)
    return fullDetails


# Remove Empty elements from list x
def removeEmptyElementFromList(givenList):
    newList = []
    for i in givenList:
        demo=[]
        for j in i:
            if j=="" or j==" ":
                pass
            else:
                demo.append(j)
        newList.append(demo)
    return newList

#for printing the list know you have
def printList(allStudentList):
    for i in allStudentList:
        print(i)
        print()
        print()
        print()

def extractFromList(studentList):
    returnDemo = []
    for i in studentList:
        demo = i.split(" ")
        demo2=[]
        for j in demo:
            if j=="" or j==" ":
                pass
            else:
                demo2.append(j)
        returnDemo.append(demo2)
    returnDemo2 = []
    for i in returnDemo:
        demo2 = []
        for j in i:
            demo = j.strip()
            demo2.append(demo)
        returnDemo2.append(demo2)
    return returnDemo2

#used to remove colon and star from the list 
def removeColonStarFromList(allStudentList):
    tempStudentList = []
    for i in allStudentList:
        demoList = []
        for j in i:
            if j==":" or j=="*" or j=="" or j==" ":
                pass
            else:
                demoList.append(j.strip('$*#'))
        tempStudentList.append(demoList)
    return tempStudentList

#used for removing the college and university names from the list
def extractTextList(allStudentList):
    demoString = allStudentList.split(' ------------------------------------------------------------------------------------------------------------------------------------')
    newList = []
    for i in demoString:
        if 'PUNE' in i:
            newList.append("")
        else:
            newList.append(i)

    newList2 = newList
    newList = []
    for i in newList2:
        if "NAME" in i:
            demo = i.split(" ----  -------------------------------------------------- -------------------- ---   ---------- --- --- -----------------------------")
            newList.append(demo[1])
        else:
            newList.append(i)

    newList2=[]
    for i in newList:
        if i==" " or i=="" or i==":":
            pass
        else:
            newList2.append(i)
    newList2.pop()
    return newList2

def nameSubjects(studentDetails):
    for i in studentDetails[1][0:(len(studentDetails[1]))]:
        i[0] = subjects[i[0]]
        
    allData = []
    for i in studentDetails:
        for j in i:
            if '410999' in j:
                pass
            else:
                allData.append(j)
    return allData

def getFirstElement(studentDetails):
    listDemo = []
    for i in studentDetails:
        listDemo.append(i[0])
    return listDemo

def removeBack(newPerfectData):
    demoData = []
    l = len(newPerfectData[0])
    for i in newPerfectData:
        if(len(i)==l):
            demoData.append(i)
    return demoData

# def getAvailableSubjects(demo):
#     list1=[]
#     for i in demo:
        

#main function begin from here
hello = 'FY'
reader = PyPDF2.PdfReader(hello+'.pdf')
string1 = ""

global subjects
subjects = {
    "310901":"DMS",
    '310902':"DSA",
    "310903":"OOP",
    "310904":"SEPM",
    "310905":"ISEE",
    "310906":"DSALab",
    "310907":"OOPLab",
    "310908":"PLab",
    "310909":"BCLab",
    "310910":"AudCou1",
    "310912":"DBMS",
    "310913":"CN",
    "310914":"JP",
    "310915":"OS",
    "310916":"Elective1",
    "310917":"DBMSLab",
    "310918":"OSLab",
    "310919":"JPLab",
    "310920":"PBL-I",
    "410901":"DS",
    "410902":"WT",
    "410903":"CC",
    "410904":"Elective2",
    "410905":"STQA",
    "410906":"WTLab",
    "410907":"CL",
    "410908":"DSLab",
    "410909":"PBL-II",
    "410999":"UnKnown",
    "410912":"MajorProject",
    "410913":"SOMP",
    "210241" : "Discrete Mathematics",
    "210242" : "Fundamentals of Data Structures",
    "210243" : " (OOP)",
    "210244" : "Computer Graphics",
    "210245" : "Digital Electronics and Logic Design",
    "210246" : "Data Structures Laboratory",
    "210247" : "OOP and Computer Graphics Laboratory",
    "210248" : "Digital Electronics Laboratory",
    "210249" : "Business Communication Skills",
    "210250": "Humanity and Social Science",
    "210251": "Audit Course 3",
    "207003": "Engineering Mathematics III",
    "210252": "Data Structures and Algorithms",
    "210253": "Software Engineering",
    "210254": "Microprocessor",
    "210255": "Principles of Programming Languages",
    "210256": "Data Structures and Algorithms Laboratory",
    "210257": "Microprocessor Laboratory",
    "210258": "Project Based Learning II",
    "210259": "Code of Conduct",
    "210260": "Audit Course 4",
}


for i in range(len(reader.pages)):
    page = reader.pages[i]
    string1 = string1 + page.extract_text(); 

allStudentList = extractTextList(string1)
allStudentList = extractFromList(allStudentList)
allStudentList = removeEmptyElementFromList(allStudentList)
allStudentList = removeColonStarFromList(allStudentList)

perfectData = []

temp = allStudentList[0]
global semester
i=0 
while(len(temp[i])>1 or not(temp[i].isnumeric())):
    i = i+1
semester = int(temp[i])


for i in allStudentList:
    demoMarks1 = intializeAll(i)
    demoMarks1 = nameSubjects(demoMarks1)
    perfectData.append(demoMarks1)

perfectData=removeBack(perfectData)
lent = len(perfectData[0])
newPerfectData = []
for i in perfectData:
    newPerfectData.append(i[0:lent])

demoData = []

for i in newPerfectData:
    demoData1 = []
    for j in i:
        demoData2 = []
        for k in j:
            if k=="" or k==" ":
                pass    
            else:
                demoData2.append(k)
        demoData1.append(demoData2)
    demoData.append(demoData1)

newPerfectData = demoData
list1 = []
for i in newPerfectData:
    for j in i:
        if ':!' in j:
            j.remove(':!')



allElements = getFirstElement(newPerfectData[0])
subjectsAvailable = allElements[6+semester:]
print(subjectsAvailable)
newDict = dict()
for i in allElements:
    newDict[i]=[]

for i in newPerfectData:
    for j in i:
        try:
            newDict[j[0]].append(j[1:])
        except:
            pass


#This is pandas dataframe used to convert the dictionary to dataframe 
for keys, values in newDict.items():
    if(len(values[0])==5):
        df = pd.DataFrame(newDict[keys], columns=[keys+'Int',keys+'Ext', keys+'Tot', keys+'Grd', keys+'Cred'])
        df[keys+'Tot'] = df[keys+'Tot'].replace('AB', '-1')
        df[keys+'Tot'] = df[keys+'Tot'].astype('int')
        newDict[keys]=df
    elif(len(values[0])==4):
        df = pd.DataFrame(newDict[keys], columns=[keys+'Int', keys+'Tot', keys+'Grd', keys+'Cred'])
        df[keys+'Tot'] = df[keys+'Tot'].replace('AB', '-1')
        df[keys+'Tot'] = df[keys+'Tot'].astype('int')
        newDict[keys]=df
    else:
        df = pd.DataFrame(newDict[keys], columns=[keys])
        newDict[keys]=df    

# this is used to merge all the data frames column wise
merged_df = pd.DataFrame()
for key in newDict:
    df = newDict[key]
    merged_df = pd.concat([merged_df, df], axis=1)

k = 'Sem'+str(semester)

#this is to convert the dataframe in excel
# newMergedDf = pd.DataFrame(merged_df)
print(merged_df)

# toppers dataframe
merged_df[k] = merged_df[k].astype('float')
toppers = pd.concat([merged_df.nlargest(10, k)['name'],merged_df.nlargest(10, k)[k]], axis=1, join='inner')
print(toppers)

subToppers = []

df = merged_df
field='DMSTot'
for i in subjectsAvailable:
    field = i+'Tot'
    df_new = pd.concat([df[df[field]==max(df[field])]['name'],df[df[field]==max(df[field])][field]], axis=1, join='inner')
    df_new.rename(columns={field:"Marks"}, inplace=True)
    subToppers.append(df_new)

#subject Toppers dataframe
df_subToppers = pd.concat(subToppers,keys=subjectsAvailable)

subMarksCount=[]
demoDict = {}

allFields = {
    0:'Marks40To49',
    1:'Marks50To54',
    2:'Marks55To59',
    3:'Marks60To65',
    4:'greaterThan66',
    5:'failCount',
    6:'passCount',
    7:'failurePercent',
    8:'passingPercent'
}

#for the sheet SubjectWiseCount
for i in subjectsAvailable:
    field = i+'Tot'
    field2 = i+'Cred'
    demoList = []
    totalCount = df[field].count()
    betWeen40To49 = df[field][(df[field]>=40) & (df[field]<=49)].count()
    betWeen50To54 = df[field][(df[field]>=50) & (df[field]<=54)].count()
    betWeen55To59 = df[field][(df[field]>=55) & (df[field]<=59)].count()
    betWeen60To65 = df[field][(df[field]>=60) & (df[field]<=65)].count()    
    greaterThan66 = df[field][df[field]>=66].count()    
    failCount = df[field2][df[field2]=='FF'].count()    
    passCount = totalCount - failCount
    failurePercent = round((failCount*100)/totalCount,4)
    passingPercent = round((passCount*100)/totalCount,4)

    demoList.append(betWeen40To49)
    demoList.append(betWeen50To54)
    demoList.append(betWeen55To59)
    demoList.append(betWeen60To65)
    demoList.append(greaterThan66)
    demoList.append(failCount)
    demoList.append(passCount)
    demoList.append(failurePercent)
    demoList.append(passingPercent)
    
    demoDict[i] = demoList
    
#Excel in the all the count of the internal and external marks 
countPassed = pd.DataFrame(demoDict)
countPassed = countPassed.rename(index=allFields)
print(countPassed)

with pd.ExcelWriter(hello+'.xlsx') as Writer:
    merged_df.to_excel(Writer, sheet_name='AllStudentList')
    toppers.to_excel(Writer, sheet_name='Toppers')
    df_subToppers.to_excel(Writer, sheet_name='Subject Toppers')
    countPassed.to_excel(Writer, sheet_name='SubjetWiseCount')