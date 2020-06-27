from django.db import models
from django.contrib.auth.models import User
from resume.models import Resume_Detail

# Create your models here.
class Company_Coming(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    company_id = models.AutoField(primary_key = True)
    company_name = models.CharField(max_length = 100)
    job_description = models.TextField(max_length = 250)
    company_location = models.CharField(max_length = 70)
    branch_cse = models.BooleanField(default = False)
    branch_ceit = models.BooleanField(default = False)
    branch_it = models.BooleanField(default = False)
    branch_ec = models.BooleanField(default = False)
    branch_en = models.BooleanField(default = False)
    branch_ce = models.BooleanField(default = False)
    branch_me = models.BooleanField(default = False)
    branch_mca = models.BooleanField(default = False)
    branch_mba = models.BooleanField(default = False)
    branch_cse = models.BooleanField(default = False)
    students_applied = models.CharField(max_length = 1500)

    def __str__(self):
        return self.company_name