import PyPDF2
import pandas as pd 
import matplotlib as plt 
import DataManipulation as dm 

#This is the main file 
global semester
global subjects
hello = "FY"
reader = PyPDF2.PdfReader(hello+".pdf")
allStudentData=""
for i in range(len(reader.pages)):
    page = reader.pages[i]
    allStudentData = allStudentData + page.extract_text(); 

allStudentData = dm.dataFilter(allStudentData)
semester = dm.getSem(allStudentData[0])

subjects = dm.getAllSubjects()
newdata = allStudentData
allStudentData = []

for i in newdata:
    demo = dm.intializeAll(i, semester)
    allStudentData.append(demo)


newdata = allStudentData
allStudentData = []

for i in newdata: 
    demo = dm.nameSubjects(i, subjects)
    allStudentData.append(demo)



allStudentData = dm.clarifyStudentYearWise(allStudentData)
# for i in allStudentData:
#     print()
#     print()
#     print()
#     print()
#     print()
#     print("--------------------------------------------------------------")
#     print()
#     print()
#     print()
#     print()
#     print(i)
