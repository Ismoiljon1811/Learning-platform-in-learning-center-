from django.urls import path
from .views import TeacherDashboardView, TeacherTeamsView, LessonView, HomeworkGetView, StudentsGroupView, HomeworkGetViewS


app_name = 'teachers'

urlpatterns = [
    path('teacher/', TeacherDashboardView.as_view(), name='teacher'),
    path('guruhlarim/<int:teacher_id>/', TeacherTeamsView.as_view(), name='guruhlarim'),
    path('lessons/<int:group_id>/', LessonView.as_view(), name='lessons'),
    path('homework/<int:team_id>/', HomeworkGetView.as_view(), name='homework'),
    path('student-homework/<int:team_id>/', HomeworkGetViewS.as_view(), name='student_homework'),
    path('student/<int:team_id>/', StudentsGroupView.as_view(), name='student'),
]