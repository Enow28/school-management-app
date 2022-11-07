
class student_class:
    Fees=300000
    def __init__ (self, first_name, Second_name, Class, sex, fees=0, has_paid=False ):
        self.first_name=first_name
        self.Second_name=Second_name
        self.Class=Class
        self.sex=sex
        self.fees=fees
        self.has_paid=has_paid
     
    def info(self):
        return self.first_name + " ; " + self.Second_name + " ; " + self.Class + " ; " +self.sex + " ; " +  str(self.fees) +" ; " + str(self.has_paid) 
    def total_student_paid():
        number_paid=0
        if number_paid==True:
            number_paid+=1
        return number_paid
    def total_student_owing(self):
        number_owing=0
        if self.has_paid==False:
            number_owing+=1
        return number_owing
    def update_fees(FEES:int):
        student_class.fees=FEES
