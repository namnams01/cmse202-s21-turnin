# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, year = 0):
        self.name = name
        self.gpa = gpa
        self.year = year
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        
    def enroll(self, list=[]):
        self.enroll = list
        return
    def display_classes(self):
        print('I am currently enrolled in', self.enroll)
        return
    def years_until_graduation(self):
        years = 4 - self.year
        if years ==0:
            print('I am graduating this year')
        else:
            print('I am graduating in',years,'years')
        

class Spartan(Student):
    
    def motto(self, motto = ''):
        self.motto = motto
    def school_spirit(self):
        print('My name is', self.name)
        print('I am a Spartan. My motto is', self.motto)
    