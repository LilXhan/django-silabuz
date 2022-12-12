from django.db import models

# Vamos a crear 4 modelos: Person, Student, Teacher, Classroom

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    sur_name = models.CharField(max_length=200)
    born_date = models.DateField()

    class Meta:
        abstract = True

class Teacher(Person):
    salary = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return self.first_name


class ClassRoom(models.Model):
    idTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=2)
    start_time = models.TimeField()

    def __str__(self): # <QuerySet [<ClassRoom: A>, <ClassRoom: B>, <ClassRoom: C>, <ClassRoom: D>]>
        return self.name
        
    class Meta: # renombrar tabla
        db_table = 'classrooms'


class Student(Person):
    idClassroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    grade_lab = models.FloatField(default=0.0)
    grade_exam = models.FloatField(default=0.0)
    grade_final = models.FloatField(default=0.0)

    class Meta:
        db_table = 'students'


class StudentProxy(Student):

    class Meta:
        ordering = ["id"]       
        proxy = True

    def average(self):
        return self.grade_exam * 0.10 + self.grade_lab * 0.60 + self.grade_final * 0.30



class TeacherProxy(Teacher):

    class Meta:
        proxy = True

    def get_bonus(self):
        return self.salary + self.rating * 100


class Evaluation(models.Model):
    date_time = models.DateTimeField()
    grade = models.CharField(max_length=30)
    evaluator = models.CharField(max_length=50)


    class Meta:
        abstract = True


class ExamFinal(Evaluation):
    exam_duration_min = models.IntegerField(default=0)
    number_questions = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)


    def point_question(self):
        return self.total_score / self.number_questions


class Project(Evaluation):
    theme_project = models.CharField(max_length=100)
    numbers_groups = models.IntegerField(default=0)


class ProjectProxy(Project):

    class Meta:
        ordering = ["theme_project"]
        proxy = True

    