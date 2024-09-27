from django.shortcuts import render, get_object_or_404
from django.views import View
from users.permissions import TeacherRequiredMixin
from users.models import Teacher, Team, Student
from students.models import Homework


class TeacherDashboardView(TeacherRequiredMixin, View):
    def get(self, request): 
        return render(request, 'teachers/teachers_dashboard.html')
    


class TeacherTeamsView(TeacherRequiredMixin, View):
    def get(self, request,teacher_id):
        teams = Team.objects.filter(id = teacher_id)
        return render(request, 'teachers/guruhlarim.html',{"teams": teams})
    

class LessonView(TeacherRequiredMixin,View):
    def get(self, request, group_id):
        team = get_object_or_404(Team, id=group_id)
        lessons = team.lessons.all()
        return render(request, 'teachers/lessons.html', context={"lessons":lessons, "team": team})
    

class HomeworkGetView(TeacherRequiredMixin,View):
    def get(self, request,team_id):
        team = get_object_or_404(Team, id=team_id)
        homeworks = team.team.all()
        return render(request,'teachers/homework.html',{'homeworks':homeworks, "team": team})
     

class HomeworkGetViewS(TeacherRequiredMixin,View):
    def get(self, request,team_id):
        team = get_object_or_404(Team, id=team_id)
        homeworkes = team.team.all()
        return render(request,'teachers/student_homework.html',{'homeworks':homeworkes, "team": team})


class StudentsGroupView(TeacherRequiredMixin,View):
    def get(self, request,team_id):
        team = get_object_or_404(Team, id=team_id)
        students = team.students.all()
        print(students)
        return render(request,'teachers/students.html',{'students':students, "team": team})

