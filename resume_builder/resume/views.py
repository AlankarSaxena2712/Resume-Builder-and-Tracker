from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def resume_personal(request):
    return render(request, 'resume_personal.html')

def resume_career(request):
    return render(request, 'resume_career.html')

def resume_tech_skils(request):
    return render(request, 'resume-tech-skills.html')

def resume_academic(request):
    return render(request, 'resume_personal.html')

def resume_other_qual(request):
    return render(request, 'resume_personal.html')

def resume_train_certi(request):
    return render(request, 'resume_personal.html')

def resume_skills_achieve(request):
    return render(request, 'resume_personal.html')

def resume_co_curricular(request):
    return render(request, 'resume_personal.html')

def resume_references(request):
    return render(request, 'resume_personal.html')