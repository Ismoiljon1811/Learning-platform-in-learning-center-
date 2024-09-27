from django.urls import path
from .views import StudentDashboardView, StudentGroupView, StudentLessonView, HomeworkView, HomeworkGView

app_name = 'students'

urlpatterns = [
    path('dashboard/', StudentDashboardView.as_view(), name='dashboard'),
    path('guruhlarim/', StudentGroupView.as_view(), name='guruhlarim'),
    path('lesson/<int:group_id>/', StudentLessonView.as_view(), name='lessons'),
    path('homework/<int:lesson_id>/', HomeworkView.as_view(), name='homeworks'),
    path('homework-g/<int:lesson_id>/', HomeworkGView.as_view(), name='homeworks_g')
]