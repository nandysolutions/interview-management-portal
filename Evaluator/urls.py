from django.urls import path
from django.contrib.auth import login,logout
from django.urls import reverse
from Evaluator import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('login/', login, {'template_name': 'login.html'}),
    path('login/', views.user_login, name='login_users'),

    path('logout/', logout, {'template_name': 'logout.html'}),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='registe'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('userDetails/<int:user_pk>/', views.get_details_user, name='user_details'),

    # Question URLs
    path('questions/', views.all_questions, name='question_list'),
    path('question/details/<int:question_id>/', views.question_details, name='question_details'),
    path('addQuestion/', views.create_question, name='add_question'),
    path('editQuestion/<int:que_pk>/', views.edit_question, name='edit_question'),

    # Interview URLs
    path('addInterview/', views.add_interview, name='add_interview'),
    path('allInterview/', views.all_interviews, name='all_interview'),
    path('detailInterview/<int:interview_pk>/', views.interviews_details, name='interview_details'),
    path('editInterview/<int:interview_pk>/', views.edit_interview, name='edit_interview'),
    path('calendar/<int:year>/<int:month>', views.calendar, name='calenda'),
    path('allInterview/onDate/<int:year>/<int:month>/<int:day>', views.get_interviews_by_date, name='interviewsbydate'),

    # Candidate URLS
    path('candidateDetails/<int:candidate_pk>/', views.candi_details, name='candi_details'),
    path('addCandidate/', views.add_candidate, name='add_candidate'),
    path('editCandidate/<int:candidate_pk>/', views.edit_candidate, name='edit_candidate'),
    path('allCandidates/', views.all_candidates, name='all_candidates'),
    path('bulkCreateCandis/', views.bulk_upload_candis, name='bulk_upload_candis'),

    # Exam URLs
    path('Exams/', views.exams, name="allexams"),
    #path('addexam/', views.create_exam, name="createExam"),
    #path('exam/(?P<exam_pk>\d+)/', views.exam_details, name='examDetails'),
    path('examPreface/', views.exam_launch_page, name='examLaunch'),

    # Question Set URLs
    path('questionSets/', views.get_question_sets, name="allQueSets"),
    path('addQuestionSet/', views.create_question_set, name="createQuestionSet"),
    path('qset/<int:qset_pk>/', views.question_set_details, name='question_set_details'),

    # Vendor URLs
    path('allVendors/', views.allVendors, name="allVendors"),
    path('vendorDetails/<int:vendor_pk>/', views.vendor_details, name="vendor_details"),


    # Rating Sheet
    path('addRating/interview/<int:interview_pk>/round/<int:round_pk>/', views.add_ratings, name='addRating'),
    path('ratingDetails/<int:rating_pk>/', views.rating_details, name='rating_details'),

    path('sitesearch/', views.search_all, name='globalsearch'),

    # Job Openings
    path('allOpenings/', views.all_openings, name='allOpenings'),
    path('addJobOpening/', views.create_opening, name='create_opening'),
    path('editJobOpening/<int:opening_pk>/', views.edit_job_opening, name='edit_job_opening'),
    ]
