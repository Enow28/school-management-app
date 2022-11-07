from dataclasses import replace
import studentclass as stu
import uuid
#  this Method is for registration
def Register(): 
    first_name=input("enter first name: ")
    Second_name=input("enter Second name: ")
    Class=input("enter student Class: ")
    sex=input("enter student sex: ")
    student_Id=str(uuid.uuid4())
    fees=input("Enter fees:")
    first_name=stu.student_class(first_name, Second_name, Class, sex, student_Id, fees)
    with open('student.txt', 'a') as f:
        f.write(first_name.info())
        f.write('\n')

def Get_Total_student_paid():
    StudentFile=open("student.txt","r")
    StudentFileLines=StudentFile.readlines()
    Total_Student_paid=0
    for line in StudentFileLines:
        first_name,second_name,Class,sex,student_Id,fees,has_paid=line.split(";")
        print(fees)
        newfee=int(fees)
        if newfee==stu.student_class. Fees:
            Total_Student_paid = Total_Student_paid + 1
        print(Total_Student_paid)
    return Total_Student_paid

def Get_Total_student_owing():
    StudentFile=open("student.txt","r")
    StudentFileLines=StudentFile.readlines()
    Total_Student_owing=0
    for line in StudentFileLines:
        first_name,second_name,Class,sex,fees,has_paid=line.split(";")
        newfee=int(fees)
        if newfee < 300000:
            Total_Student_owing += 1
    return Total_Student_owing


def UpdateFees(name:str):
    StudentFile=open("student.txt","r") 
    StudentFileLines=StudentFile.readlines()
    Newfee=int(input("enter the amount you want to pay: "))
    n=len(StudentFileLines)
    studentexist=False
    for i in range (n):
        first_name,second_name,Class,sex,fees,has_paid=StudentFileLines[i].split(";")
        newfirst_name=first_name.replace(" ","")
        newname=name.replace(" ","")
        fees2=int(fees)
        if newname == newfirst_name:
           studentexist=True
           test=False
           finalFee=fees2 + Newfee
           if finalFee>300000:
               change=finalFee-300000
               test=True

               finalFee=300000
               

           newstudent=first_name + " ; " + second_name + " ; " + Class + " ; " +sex + " ; " +  str(finalFee) +" ; " + str(has_paid)
           StudentFileLines[i]=newstudent
           StudentFile=open("student.txt","w")
           StudentFile.writelines(StudentFileLines)
           StudentFile.close() 
           print("      ",first_name, "Fees have been updated from: ", fees, "To", finalFee )
           if test:
            print("we owe you: ", change)
           break

    if not studentexist:    
            print("The student called: ", name, "Is not a student in this School")






        # first_name,second_name,Class,sex,fees,has_paid=line.split(";")
        # newfirst_name=first_name.replace(" ","")
        # newname=name.replace(" ","")
        # fees2=int(fees)
        # if newname == newfirst_name:
        # #    print("ok")
        #    finalFee=fees2 + Newfee
        #    print("      ",first_name, "Fees have been updated from: ", fees, "To", finalFee )
        #    break

        # else:
        #     print("The student called: ", name, "Is not a student in this School")
