#Arbitrary number of arguments

def students(*student_name):
    print(student_name,type(student_name))
    for student in student_name:
        print(student)


students('Bill','Steve','Mark','Gebb','Jec','Abel')
students()
students('Jack')        
print("-----------------------------------")

#Positional and Arbitrary arguments mixing


def stud(captain,*other_students):
    print('Captain',captain)
    print('Others',other_students)

stud("Gebb","John","Dods","Edelyn")
print("-----------------------------------")

#Arbitrary keyword arguments
def stud3(captain,**other_students): 
      print('Captain',captain)
      print('Others',other_students)

stud3(captain="Gebb Ebero",second_captain="Edelyn Garcia",third_captain="Ines Ebero")

stud3(captain="Edz")