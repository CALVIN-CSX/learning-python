class Student:
     count=0
     total_gpa=0
     def __init__(self, name, gpa):
         self.name = name
         self.gpa = gpa
         Student.count+=1
         Student.total_gpa+=gpa
     #INSTANCE Method
     def get_info(self):
         return f"{self.name} {self.gpa}"
     @classmethod
     def get_count(cls):
         return cls.count
     @classmethod
     def get_average_gpa(cls):
         if cls.total_gpa==0:
             return 0
         else:
             return round(cls.total_gpa/cls.count)
student1=Student("John",40)
student2=Student("mike",50)
print(Student.get_average_gpa(),Student.get_count())