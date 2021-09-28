from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from classnote.views import register


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='click'),
    path('create/', views.create, name='click'),
    path('join/', views.join, name="join"),
    path('register/', views.register, name="register"),
    path("api/", views.classList.as_view()),
    path("api/pdf/", views.pdfList.as_view()),
    path("api/<int:pk>", views.classDetail.as_view()),
    path('token/', obtain_auth_token, name='login'),
    path('landing/', views.home, name='home'),
    path('pdf-viewer/', views.pdfviewer, name="pdf-viewer"),
    path('class/', views.classUI, name="classUI"),
    path('pdf/', views.pdf, name="pdf"),
    path('profile/', views.profile, name="profile"),
    path('student-register/', views.StudentRegister, name="studentRegister"),
    path('teacher-profile/', views.teacherProfile, name="teacherProfile"),
    path('pdf-upload', views.BookUploadView, name="pdf-uplaod")

]
