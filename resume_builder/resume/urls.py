from django.urls import path, include
from .views import home, resume_personal, resume_academic, resume_career, resume_co_curricular, resume_other_qual, resume_references, resume_skills_achieve, resume_tech_skils, resume_train_certi

urlpatterns = [
    path('', home, name = 'home'),
    path('resume-personal/', resume_personal, name = 'reume_personal'),
    path('resume-career/', resume_career, name = 'reume_career'),
    path('resume-tech-skills/', resume_tech_skils, name = 'reume_tech_skills'),
    path('resume-academic/', resume_academic, name = 'reume_academic'),
    path('resume-other-qual/', resume_other_qual, name = 'reume_other_qual'),
    path('resume-train-certi/', resume_train_certi, name = 'reume_train_certi'),
    path('resume-skills-achieve/', resume_skills_achieve, name = 'reume_skills_achieve'),
    path('resume-co-curricular/', resume_co_curricular, name = 'reume_co_curricular'),
    path('resume-references/', resume_references, name = 'reume_references'),
]
