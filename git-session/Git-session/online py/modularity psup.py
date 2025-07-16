#modularity: multiples functions to perform diff actions inside classes
class Student:
    def _init_(self,name,age,marks):
        self.name=name 
        self.age= age 
        self.marks=marks

    def display_info(self):
        print(f"name: {self.name},age:{self.age}, Marks: {self.marks}")
    
    def get_student_details(self):
        if self.marks>=40:
            print(f"{self.name}has passed@!")
        else:
            print(f"{self.name}has failed")

#create objescts
student1=Student("naren",30,50)
student2=Student("Sam",20,30)f

#calling fn
student1.display_info()
student1.get_student_details()
student2.display_info()
student2.display_info()
student2.get_student_details()