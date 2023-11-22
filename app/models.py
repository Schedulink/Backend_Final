from django.db import models


class Department(models.Model):
    dept_name=models.CharField(blank=False,max_length=40,primary_key=True)

    class Meta:
        verbose_name_plural ="1. Departments"

class Degreeprogram(models.Model):
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    deg_name=models.CharField(primary_key=True,max_length=40,blank=False)

    class Meta:
        verbose_name_plural ="2. Degreeprograms"

class Semester(models.Model):
    sem_id=models.IntegerField(blank=False,primary_key=True)
    sem_num=models.IntegerField(blank=False)
    deg_name=models.ForeignKey(Degreeprogram,on_delete=models.CASCADE)
    reg_year=models.CharField(max_length=50)
    sem_type = models.CharField(max_length=10,blank=False)

    class Meta:
        verbose_name_plural ="3. Semester"

class Subject(models.Model):
    sem_id=models.ForeignKey(Semester,on_delete=models.CASCADE)
    sub_code=models.CharField(max_length=20,blank=False,primary_key=True)
    sub_title=models.CharField(max_length=100,blank=False)
    reg_year=models.CharField(max_length=50)
    tcp=models.IntegerField(blank=False)

    class Meta:
        verbose_name_plural ="4. Subject"

class Faculty(models.Model):
    fac_id=models.IntegerField(blank=False,primary_key=True)
    fac_name=models.CharField(max_length=40,blank=False)
    sub_code=models.ForeignKey(Subject,on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=100,blank=False)
    dept_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    tcp=models.IntegerField(blank=False,default=False)

    class Meta:
        verbose_name_plural ="5. Faculty"

class TimetableData(models.Model):
    s_no = models.IntegerField(blank=False)
    sub_code = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='timetable_entries')
    sub_title = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='+')
    fac_name = models.ForeignKey(Faculty,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural ="6. TimetableData"

class Admin(models.Model):
    fac_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    password = models.CharField(max_length=150,blank=False,unique=True,primary_key=True)
    email_id  = models.EmailField(max_length=150,blank=False,unique=True)

    class Meta:
        verbose_name_plural ="7. Admin"