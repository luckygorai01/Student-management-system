from django.db import models
from adminapp.models import StudentList
# Create your models here.

class addcourse(models.Model):
    COURSE_CHOICES = [
        ('AOOP',"ADVANCED OBJECT ORIENTED PROGRAMMING"),
        ("CTOD","COMPUTATIONAL THINKING FOR OBJECT DESIGN"),
        ("CTOOD","COMPUTATIONAL THINKING FOR OBJECT ORIENTED DESIGN"),
        ("PFSD","PYTHON FULL STACK WEB DEVELOPMENT"),
        ("DBMS","DATABASE MANAGEMENT SYSTEM"),
        ("DSS","DATA SCIENCE AND STATISTICS"),
        # ("DSS","DATA SCIENCE AND STATISTICS"),
        
    ]
    SECTION_CHOICES = [
        ('S11','SECTION S11'),
        ('S12','SECTION S12'),
        ('S13','SECTION S13'),
        ('S14','SECTION S14'),
        ('S15','SECTION S15'),
        ('S21','SECTION S21'),
        ('S22','SECTION S22'),
        ('S23','SECTION S23'),
        ('S24','SECTION S24'),
        ('S25','SECTION S25'),
    ]
    student = models.ForeignKey(StudentList,on_delete=models.CASCADE)
    course = models.CharField(max_length=50,choices=COURSE_CHOICES)
    section = models.CharField(max_length=50,choices=SECTION_CHOICES)
    
def str(self):
    return f'{self.student.Register_Number} - {self.course} ({self.section})'

class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP',"ADVANCED OBJECT ORIENTED PROGRAMMING"),
        ("CTOD","COMPUTATIONAL THINKING FOR OBJECT DESIGN"),
        ("CTOOD","COMPUTATIONAL THINKING FOR OBJECT ORIENTED DESIGN"),
        ("PFSD","PYTHON FULL STACK WEB DEVELOPMENT"),
        ("DBMS","DATABASE MANAGEMENT SYSTEM"),
        ("DSS","DATA SCIENCE AND STATISTICS"),
        # ("DSS","DATA SCIENCE AND STATISTICS"),
        
    ]
    student = models.ForeignKey(StudentList,on_delete=models.CASCADE)
    course = models.CharField(max_length=50,choices=COURSE_CHOICES)
    marks = models.IntegerField()
    
    def str(self):
        return f'{self.student.Register_Number} - {self.course}'