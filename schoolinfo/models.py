from django.db import models

# Create your models here.
class department(models.Model):
    department_name = models.CharField(max_length=70)

    def __str__(self):
        return self.department_name


class course_year(models.Model):
    course_year = models.CharField(max_length=70)

    def __str__(self):
        return self.course_year


gender_choice=(('male','male'),
               ('female','female'))

class students(models.Model):
    student_name = models.CharField(max_length=70)
    student_age = models.IntegerField()
    student_gender = models.CharField(choices=gender_choice,max_length=70)
    course_year = models.ForeignKey(course_year,on_delete=models.CASCADE)
    department = models.ForeignKey(department,on_delete=models.CASCADE)


    def __str__(self):
        return self.student_name



class professor(models.Model):
    professor_name = models.CharField(max_length=70)
    professor_age = models.CharField(max_length=70)
    professor_gender = models.CharField(max_length=70)
    professor_subject = models.CharField(max_length=70)
    department = models.ForeignKey(department,on_delete=models.CASCADE)


    def __str__(self):
        return self.professor_name