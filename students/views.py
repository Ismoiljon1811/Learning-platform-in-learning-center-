from django.shortcuts import render, get_object_or_404, redirect
from users.permissions import StudentRequiredMixin
from django.views import View
from users.models import Student, Team
from .forms import HomeworkFrom, HomeworkGForm
from .models import Lesson, Homework

class StudentDashboardView(StudentRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')

class StudentGroupView(StudentRequiredMixin, View):
    def get(self,request):
        student = Student.objects.get(user=request.user)
        return render(request, 'students/guruhlarim.html', {'student': student})


class StudentLessonView(StudentRequiredMixin, View):
    def get(self, request, group_id):
        team = get_object_or_404(Team, id=group_id)
        lessons = team.lessons.all()
        return render(request, 'students/lessons.html', {'lessons': lessons})


class HomeworkView(StudentRequiredMixin, View):
    def get(self, request, lesson_id):
        form = HomeworkFrom()
        return render(request, 'students/homework.html', {'form':form})

    def post(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        student = get_object_or_404(Student, user=request.user)

        form = HomeworkFrom(request.POST, request.FILES)
        if form.is_valid():
            homework = Homework()
            homework.student = student
            homework.lesson = lesson
            homework.dascription = form.cleaned_data['dascription']
            homework.homework_file = form.cleaned_data['homework_file']
            homework.save()

            lesson.homework_status = True
            lesson.save()
            print(homework)

            return redirect('students:dashboard')
        

class HomeworkGView(StudentRequiredMixin, View):
    def get(self, request, lesson_id):
        
        home = Homework.objects.filter(lesson_id=lesson_id)
        homeworks = HomeworkGForm()
        homeworks.dascription = 'dascription'
        print(homeworks)
        print(home)
        return render(request, 'students/homework_g.html',{'homeworks':homeworks, 'homes':home})