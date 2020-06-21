from django.urls import path
from .views import resume_personal, resume_academic, resume_career, resume_co_curricular, resume_other_qual, resume_references, resume_skills_achieve, resume_tech_skils, resume_train_certi, resume_print

urlpatterns = [
    path('resume-personal/', resume_personal, name = 'resume_personal'),
    path('resume-career/', resume_career, name = 'resume_career'),
    path('resume-tech-skills/', resume_tech_skils, name = 'resume_tech_skills'),
    path('resume-academic/', resume_academic, name = 'resume_academic'),
    path('resume-other-qual/', resume_other_qual, name = 'resume_other_qual'),
    path('resume-train-certi/', resume_train_certi, name = 'resume_train_certi'),
    path('resume-skills-achieve/', resume_skills_achieve, name = 'resume_skills_achieve'),
    path('resume-co-curricular/', resume_co_curricular, name = 'resume_co_curricular'),
    path('resume-references/', resume_references, name = 'resume_references'),
    path('resume-print/', resume_print, name = 'resume_print'),
] 