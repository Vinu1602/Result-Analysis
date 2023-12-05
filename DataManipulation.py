
#Removes the empty elemnent from the list
def removeEmptyElements(my_list):
    updated_list = []
    for i in my_list: 
        if i=="" or i==" " or i=="  ":
            pass
        else: 
            updated_list.append(i)
    return updated_list

#Accepts All the student data in the text form and then return it in list form by filtering
def dataFilter(allStudentList):
    allStudentList = extractTextList(allStudentList)
    allStudentList = extractFromList(allStudentList)
    allStudentList = removeEmptyElementFromList(allStudentList)
    allStudentList = removeColonStarFromList(allStudentList)
    allStudentList = removeColonExclamation(allStudentList)
    return allStudentList

#separates the data student wise and inside the student wise it is separated in the elements like Name, studentName, marks, grade, etc....... it includes the empty elements too
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

# function used for removing the empty elements from the list 
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

#Remove the Colon and start from the list or dollar sign which is in the result indicating a student is fail or not
def removeColonStarFromList(allStudentList):
    tempStudentList = []
    for i in allStudentList:
        demoList = []
        for j in i:
            if j==":" or j=="*" or j=="" or j==" " or j==":!":
                pass
            else:
                demoList.append(j.strip('$*#'))
        tempStudentList.append(demoList)
    return tempStudentList


#function is used to get the semester at which result is this 
def getSem (temp):
    i=0
    while(len(temp[i])>1 or not(temp[i].isnumeric())):
        i = i+1
    return int(temp[i])


def getAllSubjects():
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
        "210241":"Discrete Mathematics",
        "210242":"Fundamentals of Data Structures",
        "210243":" (OOP)",
        "210244":"Computer Graphics",
        "210245":"Digital Electronics and Logic Design",
        "210246":"Data Structures Laboratory",
        "210247":"OOP and Computer Graphics Laboratory",
        "210248":"Digital Electronics Laboratory",
        "210249":"Business Communication Skills",
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
        "310241":" Database Management Systems",
        "310242":" Theory of Computation",
        "310243":" Systems Programming and Operating System",
        "310244":" Computer Networks and Security",
        "310245":"BECE_ElectiveI",
        "310245A":" Elective I- Internet of Things and Embedded Systems",
        "310245B":" Elective I- Human Computer Interface",
        "310245C":" Elective I- Distributed Systems",
        "310245D":" Elective I- Software Project Management",
        "310246":" Database Management Systems Laboratory",
        "310247":" Computer Networks and Security Laboratory",
        "310248":" Laboratory Practice I",
        "310249":" Seminar and Technical Communication",
        "310250":" Audit Course 5",
        "310251":" Data Science and Big Data Analytics",
        "310252":" Web Technology",
        "310253":" Artificial Intelligence",
        "310254":"BECE-ElectiveII",
        "310254A":" Elective II- Information Security",
        "310254B":" Elective II- Augmented and Virtual Reality",
        "310254C":" Elective II- Cloud Computing",
        "310254D":" Elective II- Software Modeling and Architectures",
        "310255":" Internship",
        "310256":" Data Science and Big Data Analytics Laboratory",
        "310257":" Web Technology Laboratory",
        "310258":" Laboratory Practice II",
        "310259":" Audit Course 6",
        "410241":" Design and Analysis of Algorithms",
        "410242":" Machine Learning",
        "410243":" Blockchain Technology",
        "410244A":" Pervasive Computing",
        "410244B":" Multimedia Techniques",
        "410244C":" Cyber Security And Digital Forensics",
        "410244D":" Object Oriented Modeling And Design",
        "410244E":" Digital Signal Processing",
        "410245A":" Information Retrieval",
        "410245B":" GPU Programming And Architecture",
        "410245C":" Mobile Computing",
        "410245D":" Software Testing And Quality Assurance",
        "410245E":" Compilers",
        "410246":" Laboratory Practice III",
        "410247":" Laboratory Practice IV",
        "410248":" Project Stage I",
        "410249":" Audit Course 7",
        "410250":" High Performance Computing",
        "410251":" Deep Learning",
        "410252A":" Natural Language Processing",
        "410252B":" Image Processing",
        "410252C":" Software Defined Networks",
        "410252D":" Advanced Digital Signal Processing",
        "410252E":" Open Elective I",
        "410253": "Elective",
        "410253A":" Pattern Recognition",
        "410253B":" Soft Computing",
        "410253C":"Buisness Intelligence",
        "410253D":"Quantum Computing",
        "410253E":" Open Elective II",
        "410254":" Laboratory Practice V",
        "410255":" Laboratory Practice VI",
        "410256":" Project Stage II",
        "410257":" Audit Course 8",
        "107001":"Engineering Mathematics-I",
        "107002":"Engineering Physics",
        "107009":"Engineering Chemistry",
        "102003":"Systems in Mechanical Engineering",
        "103004":"Basic Electrical Engineering",
        "104010":"Basic Electronics Engineering",
        "110005":"Programming and Problem solving",
        "101011":"Engineering Mechanics",
        "111006":"Workshop",
        "101007":"Audit Course 1"
    }
    return subjects


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def intializeAll(givenStudentList, semester):
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

def removeBack(newPerfectData):
    regularStudent = []
    backStudent = []
    l = len(newPerfectData[0])
    for i in newPerfectData:
        if(len(i)==l):
            regularStudent.append(i)
        else: 
            backStudent.append(i)
    return [regularStudent, backStudent]


def nameSubjects(studentDetails, subjects):
    for i in studentDetails[1][0:(len(studentDetails[1]))]:
        i[0] = subjects[i[0]]
        
    allData = []
    for i in studentDetails:
        for j in i:
                allData.append(j)
    return allData


def clarifyStudentYearWise(newPerfectData):
    regularStudent = [[]]
    studentLengthList = []
    studentLengthList.append(len(newPerfectData[0]))
    for i in newPerfectData:
        if(len(i)==studentLengthList[-1]):
            regularStudent[-1].append(i)
            print(regularStudent[-1])
        else:
            print("===================================")
            print()
            print()
            studentLengthList.append(len(i))
            regularStudent.append([i])
            print(i)
    return regularStudent


def removeColonExclamation(studentData):
    for i in studentData:
        for j in i:
            if ':!' in j:
                j.remove(':!')
    return studentData


def getFirstElement(studentDetails):
    listDemo = []
    for i in studentDetails:
        listDemo.append(i[0])
    return listDemo