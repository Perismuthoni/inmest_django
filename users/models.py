from django.db import models

# Create your models here.


# class UserType(models.TextChoices):
#     USER_TYPES = [
#         ('EIT', 'EIT'),
#         ('TEACHING_FELLOW', 'Teaching Fellow'),
#         ('ADMIN_STAFF', 'Admin Staff'),
#         ('ADMIN', 'Admin'),
#         ]

class IMUser(models.Model):

    class UserTypes(models.TextChoices):
         EIT='eit'
         TEACHING_FELLOW='teaching_fellow'
         ADMIN_STAFF='admin_staff'
         ADMIN='admin'
    first_name=models.CharField(default ='',max_length=1000)
    last_name=models.CharField(default ='',max_length=1000)
    email=models.CharField(default ='',max_length=1000)
    is_active=models.BooleanField(default=True)
    usertype=models.CharField(choices=UserTypes.choices,max_length=1000,default=UserTypes.EIT)
    description=models.TextField(default ='N/A',blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_updated=models.DateTimeField(auto_now=True,blank=True,null=True)

    def stri(self):
        return f"{self.first_name},{self.last_name},{self.email}"
    

class Cohort(models.Model):
    name=models.CharField(max_length=1000)
    description=models.TextField(default ='N/A',blank=True,null=True)
    start_date=models.DateTimeField(blank=True,null=True)
    end_date=models.DateTimeField(blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_updated=models.DateTimeField(auto_now=True,blank=True,null=True)
    year=models.IntegerField(default=2024)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='users_cohorts_author')

    def stri(self):
        return f"{self.name}"
    

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE,related_name='members')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='cohortmembers_member')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_updated = models.DateTimeField(auto_now=True,null=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='cohortmembers_author')


    def stri(self):
        return f"{self.name}"
    