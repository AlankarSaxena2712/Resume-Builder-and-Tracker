from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from resume.models import Resume_Detail
from .models import Company_Coming

# Create your views here.

def is_company(user):
    return user.groups.filter(name = 'company').exists()

@user_passes_test(is_company, login_url = '/')
@login_required
def company_home(request):
    return render(request, 'company_home.html')

@user_passes_test(is_company, login_url = '/')
@login_required
def resumes(request):
    all_resumes = Resume_Detail.objects.all()
    return render(request, 'resumes.html', {'all_resumes': all_resumes})

@user_passes_test(is_company, login_url = '/')
@login_required
def view_resume(request, s_no):
    resume = Resume_Detail.objects.filter(s_no = s_no)
    return render(request, 'view_resume.html', {'resume':resume[0]})

@user_passes_test(is_company, login_url = '/')
@login_required
def search(request):
    query = request.GET['query']
    if len(query)>60:
        all_resumes = Resume_Detail.objects.none()
    else:
        all_resumes_first_name = Resume_Detail.objects.filter(first_name__icontains = query)
        all_resumes_last_name = Resume_Detail.objects.filter(last_name__icontains = query)
        all_resumes = all_resumes_first_name.union(all_resumes_last_name)

    if all_resumes.count() == 0:
        messages.warning(request, "No search results found! Please refine your query")
    return render(request, 'resume_search.html', {'all_resumes': all_resumes, 'query':query})

@user_passes_test(is_company, login_url = '/')
@login_required
def company_information(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        company_location = request.POST['company_location']
        job_description = request.POST['job_description']
        cse = request.POST.get('cse', 'off')
        ceit = request.POST.get('ceit', 'off')
        it = request.POST.get('it', 'off')
        ec = request.POST.get('ec', 'off')
        en = request.POST.get('en', 'off')
        me = request.POST.get('me', 'off')
        ce = request.POST.get('ce','off')
        mca = request.POST.get('mca', 'off')
        mba = request.POST.get('mba', 'off')
        branch_cse = False
        branch_ceit = False
        branch_it = False
        branch_ec = False
        branch_en = False
        branch_ce = False
        branch_me = False
        branch_mca = False
        branch_mba = False

        if cse == 'CSE':
            branch_cse = True 
        if ceit == 'CEIT':
            branch_ceit = True
        if it == 'IT':
            branch_it = True
        if ec == 'EC':
            branch_ec = True
        if en == 'EN':
            branch_en = True
        if me == 'ME':
            branch_me = True
        if ce == 'CE':
            branch_ce = True
        if mca == 'MCA':
            branch_mca = True
        if mba == 'MBA':
            branch_mba = True

        if Company_Coming.objects.filter(company_name = company_name).exists():
            Company_Coming.objects.update(
                company_name = company_name,
                job_description = job_description,
                company_location = company_location,
                branch_cse = branch_cse,
                branch_ceit = branch_ceit,
                branch_it = branch_it,
                branch_ec = branch_ec,
                branch_en = branch_en,
                branch_me = branch_me,
                branch_ce = branch_ce,
                branch_mca = branch_mca,
                branch_mba = branch_mba,
            )
            messages.success(request, f"Company information Updated! Now students can apply to you {company_name}")
            return redirect('company_home')
        else:
            company_info = Company_Coming(
                user_id = request.user.id,
                company_name = company_name,
                job_description = job_description,
                company_location = company_location,
                branch_cse = branch_cse,
                branch_ceit = branch_ceit,
                branch_it = branch_it,
                branch_ec = branch_ec,
                branch_en = branch_en,
                branch_me = branch_me,
                branch_ce = branch_ce,
                branch_mca = branch_mca,
                branch_mba = branch_mba,
            )
            company_info.save()
            messages.success(request, f"Company information Updated! Now students can apply to you {company_name}")
            return redirect('company_home')
    return render(request, 'company_home.html')
