
import studentclass as stu
import registerstudent as rs



state =True
while state:
    def menu():
        Menu={1:"register students", 2: "number of students that have paid fees", 3:"the number still owing", 4:"Update the fees of the children", 5:"quit"}
        for i,c in Menu.items():
            print(i,":",c)
        start=int(input("enter number: "))
        if start==1:
            rs.Register()
        elif start ==2:
            Total_Number_Paid=rs.Get_Total_student_paid()
            print("      ","The Total Number of Student that have paid are: ",Total_Number_Paid)
        elif start == 3:
            Total_Number_Owing=rs.Get_Total_student_owing()
            print("      ","The Total Number of Student that are(is) Owing: ",Total_Number_Owing)
        elif start == 4:
            Name=input("Enter student Name: ")
            rs.UpdateFees(Name)
        elif start == 5:
            quit()
        else: 
            print("Make a correct choice")
    menu()