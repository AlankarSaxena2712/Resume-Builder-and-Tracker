from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .models import Resume_Detail

# Create your views here.
def is_student(user):
    return user.groups.filter(name = 'resume').exists()

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_personal(request):
    if request.method == 'POST' and request.FILES['photo']:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        adm_no = request.POST.get('adm_no')
        email = request.POST.get('email')
        phn_no = request.POST.get('phn_no')
        linkedin_id = request.POST.get('linkedin_id')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        photo = request.FILES['photo']

        if request.user.username == adm_no:
            Resume_Detail.objects.filter(adm_no = request.user.username).update(
                user_id = request.user.id,
                first_name = first_name,
                last_name = last_name,
                adm_no = adm_no,
                email = email,
                phn_no = phn_no,
                linkedin_id = linkedin_id,
                address = address,
                state = state,
                city = city,
                zip_code = zip_code,
                photo = FileSystemStorage().save(photo.name, photo)
            )
            messages.success(request, "Data saved successfully")
            return redirect('resume_career')
        else:
            messages.error(request, "Data couldn't be saved!, Please check that the Username and Admission number are name")
            return redirect('resume_personal')
    return render(request, 'resume_personal.html')

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_career(request):
    if request.method == 'POST':
        career_objective = request.POST.get('resume_career_objective')
        Resume_Detail.objects.filter(adm_no = request.user.username).update(career_objective = career_objective)
        messages.success(request, "Data saved successfully")
        return redirect('resume_tech_skills')
    return render(request, 'resume_career.html')

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_tech_skils(request):
    if request.method == 'POST':
        tech_skills = request.POST.get('tech_skill_1') + "," + request.POST.get('tech_skill_2') + "," + request.POST.get('tech_skill_3') + "," + request.POST.get('tech_skill_4') + "," + request.POST.get('tech_skill_5') + "," + request.POST.get('tech_skill_6')
        Resume_Detail.objects.filter(adm_no = request.user.username).update(tech_skills = tech_skills)
        messages.success(request, "Data saved successfully")
        return redirect('resume_academic')
    return render(request, 'resume-tech-skills.html')

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_academic(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        university = request.POST.get('university')
        passing_year = request.POST.get('passing_year')
        percent_academic = request.POST.get('percent_academic')
        board_secondary_school = request.POST.get('board_secondary_school')
        passing_year_secondary_school = request.POST.get('passing_year_secondary_school')
        percent_secondary_school = request.POST.get('percent_secondary_school')
        board_high_school = request.POST.get('board_high_school')
        passing_year_high_school = request.POST.get('passing_year_high_school')
        percent_high_school = request.POST.get('percent_high_school')
        Resume_Detail.objects.filter(adm_no = request.user.username).update(
            course = course,
            branch = branch,
            university = university,
            passing_year = passing_year,
            percent_academic = percent_academic,
            board_secondary_school = board_secondary_school,
            passing_year_secondary_school = passing_year_secondary_school,
            percent_secondary_school = percent_secondary_school,
            board_high_school = board_high_school,
            passing_year_high_school = passing_year_high_school,
            percent_high_school = percent_high_school
        )
        messages.success(request, "Data saved successfully")
        return redirect('resume_other_qual')
    return render(request, 'resume_academic.html')

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_other_qual(request):
    if request.method == 'POST':
        university_diploma = request.POST.get('university_diploma')
        passing_year_diploma = request.POST.get('passing_year_diploma')
        percent_diploma = request.POST.get('percent_diploma')
        graduation_course = request.POST.get('graduation_course')
        university_other_graduation = request.POST.get('university_other_graduation')
        passing_year_other_graduation = request.POST.get('passing_year_other_graduation')
        percent_other_graduation = request.POST.get('percent_other_graduation')
        Resume_Detail.objects.filter(adm_no = request.user.username).update(
            university_diploma = university_diploma,
            passing_year_diploma = passing_year_diploma,
            percent_diploma = percent_diploma,
            graduation_course = graduation_course,
            university_other_graduation = university_other_graduation,
            passing_year_other_graduation = passing_year_other_graduation,
            percent_other_graduation = percent_other_graduation
        )
        messages.success(request, "Data saved successfully")
        return redirect('resume_train_certi')
    return render(request, 'resume-other-qual.html')

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_train_certi(request):
    if request.method == 'POST':
        certificates = request.POST.get('certificate_1') + "," + request.POST.get('certificate_2') + "," + request.POST.get('certificate_3') + "," + request.POST.get('certificate_4')
        internship_company_name = request.POST.get('internship_company_name')
        internship_project_title = request.POST.get('internship_project_title')
        internship_duration = request.POST.get('internship_duration')
        internship_project_description = request.POST.get('internship_project_description')
        Resume_Detail.objects.filter(adm_no = request.user.username).update(
            certificates = certificates,
            internship_company_name = internship_company_name,
            internship_project_title = internship_project_title,
            internship_duration = internship_duration,
            internship_project_description = internship_project_description
        )
        messages.success(request, "Data saved successfully")
        return redirect('resume_skills_achieve')
    return render(request, 'resume_training_certification.html')

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_skills_achieve(request):
    if request.method == 'POST':
        interpersonal_skills = request.POST.get('skill_1') + "," + request.POST.get('skill_2') + "," + request.POST.get('skill_3') + "," + request.POST.get('skill_4')
        achievements = request.POST.get('achievement_1') + "," + request.POST.get('achievement_2') + "," + request.POST.get('achievement_3') + "," + request.POST.get('achievement_4')
        Resume_Detail.objects.filter(adm_no = request.user.username).update(
            interpersonal_skills = interpersonal_skills,
            achievements = achievements
        )
        messages.success(request, "Data saved successfully")
        return redirect('resume_co_curricular')
    return render(request, 'resume_skills_achieve.html')

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_co_curricular(request):
    if request.method == 'POST':
        co_curriculars = request.POST.get('co_curricular_1') + "," + request.POST.get('co_curricular_2') + "," + request.POST.get('co_curricular_3') + "," + request.POST.get('co_curricular_4') + ',' + request.POST.get('co_curricular_5')
        Resume_Detail.objects.filter(adm_no = request.user.username).update(
            co_curriculars = co_curriculars
        )
        messages.success(request, "Data saved successfully")
        return redirect('resume_references')
    return render(request, 'resume_co_curricular.html')

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_references(request):
    if request.method == 'POST':
        resume_reference_name = request.POST.get('resume_reference_name')
        resume_reference_designation = request.POST.get('resume_reference_designation')
        resume_reference_organization = request.POST.get('resume_reference_organization')
        Resume_Detail.objects.filter(adm_no = request.user.username).update(
            resume_reference_name = resume_reference_name,
            resume_reference_designation = resume_reference_designation,
            resume_reference_organization = resume_reference_organization
        )
        messages.success(request, "Data saved successfully! Now you can view your resume")
        return redirect('resume_references')
    return render(request, 'resume_references.html')

@user_passes_test(is_student, login_url = '/')
@login_required
def resume_print(request):
    return render(request, 'resume_format.html')
