from django.urls import path
from . import views

urlpatterns = [
   path('', views.IndexClassroom.as_view(), name='index'),
   path('create/', views.CreateClassroom.as_view(), name='create'),
   path('delete/<int:id>', views.DeleteClassroom, name='delete'),
   path('formAlumn/', views.StudentForm.as_view(), name='create_student'),
   path('classroom/<int:id>', views.classroom, name='classroom'),
   path('classroom/delete/<int:id>', views.delete_student, name='delete_student')
]