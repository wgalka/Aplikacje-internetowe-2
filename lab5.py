class Course:
    def __init__(self, department, number, title):
        self.department = department
        self.number = number
        self.title = title

class CSCourse(Course):
    def __init__(self, department, number, title, recorded=False):
        super().__init__(department, number, title)
        self.is_recorded = recorded
                
type(a)
    #<class 'courses.Course'>
isinstance(a, Course)
    #True
isinstance(b, Course)
    #True
type(a) == type(b)
    #False
a == b
    #False
  
  
        
