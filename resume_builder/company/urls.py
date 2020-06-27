from django.urls import path
from .views import resumes, view_resume, search, company_home, company_information

urlpatterns = [
    path('', company_home, name = 'company_home'),
    path('resumes/', resumes, name = 'resumes'),
    path('view-resume/<int:s_no>/', view_resume, name = 'view-resume'),
    path('search/', search, name = 'search'),
    path('company_information/', company_information, name = 'company_information'),
]    