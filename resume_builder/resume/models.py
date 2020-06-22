from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Resume_Detail(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    s_no = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 50, default = '')
    last_name = models.CharField(max_length = 50, default = '')
    adm_no = models.CharField(max_length = 20, default = '')
    email = models.EmailField(max_length = 120, default = '')
    phn_no = models.CharField(max_length = 12, default = '')
    linkedin_id = models.CharField(max_length = 30, default = '')
    address = models.CharField(max_length = 300, default = '')
    state = models.CharField(max_length = 20, default = '')
    city = models.CharField(max_length = 20, default = '')
    zip_code = models.CharField(max_length = 8, default = '')
    photo = models.ImageField(upload_to = "resume_profile_pics", default = '')
    career_objective = models.TextField(max_length = 300, null=True)
    tech_skills = models.CharField(max_length = 220)
    course = models.CharField(max_length = 10)
    branch = models.CharField(max_length = 10)
    university = models.CharField(max_length = 20)
    passing_year = models.CharField(max_length = 6)
    percent_academic = models.FloatField(null = True)
    board_secondary_school = models.CharField(max_length = 20)
    passing_year_secondary_school = models.CharField(max_length = 6)
    percent_secondary_school = models.FloatField(null = True)
    board_high_school = models.CharField(max_length = 20)
    passing_year_high_school = models.CharField(max_length = 6)
    percent_high_school = models.FloatField(null = True)
    university_diploma = models.CharField(max_length = 50)
    passing_year_diploma = models.CharField(max_length = 6)
    percent_diploma = models.FloatField(null = True)
    graduation_course = models.CharField(max_length = 20)
    university_other_graduation = models.CharField(max_length = 20)
    passing_year_other_graduation = models.CharField(max_length = 6)
    percent_other_graduation = models.FloatField(null = True)
    certificates = models.CharField(max_length = 400)
    internship_company_name = models.CharField(max_length = 50)
    internship_project_title = models.CharField(max_length = 50)
    internship_duration = models.IntegerField(null = True)
    internship_project_description = models.TextField(max_length = 200)
    interpersonal_skills = models.CharField(max_length = 300)
    achievements = models.CharField(max_length = 300)
    co_curriculars = models.CharField(max_length = 300)
    resume_reference_name = models.CharField(max_length = 50)
    resume_reference_designation = models.CharField(max_length = 30)
    resume_reference_organization = models.CharField(max_length = 60)

    def __str__(self):
        return self.first_name + " " + self.last_name

    # def save(self):
    #     super().save()

    #     img = Image.open(self.photo.path)

    #     if img.height > 300 or img.height > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.photo.path)
    