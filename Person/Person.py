# 1번. 추상화, 캡슐화, 상속이란?
# 객체지향 프로그래밍에서는 클래스를 사용하여 객체들을 모델링하고, 필요한 부분만을 추출하여 표현함으로써 추상화를 구현합니다.
# 캡슐화는 정보 은닉을 통해 객체 내부의 세부 구현을 숨기고 외부에는 필요한 인터페이스만을 노출합니다.
# 상속은 기존의 클래스에서 정의된 속성과 메서드를 새로운 클래스에서 다시 사용할 수 있게 해주는 개념입니다. 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"name : {self.name}\nage : {self.age}"
    
    def get_job(self, job): # 2번 문제
        if self.age <20:
            print("too young!")
            self.job = "student"
            return
        
        else:
            self.job = job
    
    def print_job(self): # 2번 문제
        print(self.job)
        
# 3번 문제 
class Student(Person):
    def __init__(self, name, age, GPA):
        super().__init__(name, age)
        self.gpa = GPA
        
    def __str__(self):
        return f"{super().__str__()}\nGPA: {self.gpa}"
    
    def __eq__(self, other): # 4번
        if isinstance(other, Student):
            return self.gpa == other.gpa
        return False
    

"""
# 예시 코드.

person = Person("John", 25)
person.get_job("Engineer")
print(person)

student = Student("Alice", 18, 3.8)
student.get_job("Research Assistant")
print(student)
student.print_job()

student2 = Student("Bob", 18, 3.9)

print(student == student2)
"""