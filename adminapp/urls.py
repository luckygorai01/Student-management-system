from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.projecthomepage,name='projecthomepage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic' ),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('execptionpagelogic/',views.excecptionpagelogic,name='exceptionpagelogic'),
    path('UserRegistercall/',views.UserRegisterCall,name='UserRegisterCall'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('userloginpagecall/',views.userloginpagecall,name='userloginpagecall'),
    path('userloginlogic/',views.userloginlogic,name='userloginlogic'),
    path('add_student/',views.add_student,name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('datetimepagecall/',views.datetimepagecall,name='datetimepagecall'),
    path('datetimepagelogic/',views.datetimepagelogic,name='datetimepagelogic'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randomlogic/',views.randomlogic,name='randomlogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    
]

  