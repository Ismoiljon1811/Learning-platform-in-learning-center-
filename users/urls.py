from django.urls import path
from .views import (LoginView, RegisterView, ProfileView, EditProfileView, LogoutView,
                    GroupsView, StudentsListView, EditStudentView, DeleteStudentView,
                    StudentByTeamView, ResetPasswordView, EditTeacherView)


app_name = 'users'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
    path('groups/', GroupsView.as_view(), name='groups'),
    path('students/', StudentsListView.as_view(), name='students'),
    path('student-by-team/<int:id>/', StudentByTeamView.as_view(), name='students_by_team'),
    path('edit-student/<int:id>/', EditStudentView.as_view(), name='edit_student'),
    path('delete-student/<int:id>/', DeleteStudentView.as_view(), name='delete_student'),
    path('edit-teacher/<int:id>/', EditTeacherView.as_view(), name='edit_teacher'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]