from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm, ProfileEditForm, StudentEditForm, ResetPasswordForm, TeacherEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import AdminRequiredMixin
from .models import Student, Team, User, Teacher
from django.db.models import Q


def home(request):
    return render(request,'home.html')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:profile')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


class RegisterView(AdminRequiredMixin, View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'student':
                new_student = Student()
                new_student.user = user
                new_student.save()

            return redirect('/')
        return render(request, 'users/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')

class EditProfileView(LoginRequiredMixin,View):
    def get(self,request):
        form = ProfileEditForm(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form': form})

    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')

        form = ProfileEditForm(instance=request.user)
        return render(request, 'users/edit_profile.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class GroupsView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'users/groups.html', {'teams':teams})

class StudentsListView(AdminRequiredMixin,View):
    def get(self, request):
        if request.GET != {}:
            students = Student.objects.filter(Q(user__username__contains = request.GET['search']) | Q(team__name__contains = request.GET['search'])
                                              | Q(user__first_name__contains = request.GET['search']) | Q(user__last_name__contains = request.GET['search']))
        else:
            students = Student.objects.all()
        return render(request, 'users/students.html', {'students':students})

class StudentByTeamView(AdminRequiredMixin,View):
    def get(self, request, id):
        team = get_object_or_404(Team, id=id)
        students = team.students.all()
        return render(request, 'users/students.html', {'students': students})


class EditStudentView(AdminRequiredMixin,View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentEditForm(instance=student)
        return render(request, 'users/edit_student.html', {'form': form})

    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users:students')
        form = StudentEditForm(instance=student)
        return render(request, 'users/edit_student.html', {'form': form})


class DeleteStudentView(AdminRequiredMixin,View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        user = User.objects.get(username=student.user.username)
        student.delete()
        user.delete()
        return redirect('users:students')



class ResetPasswordView(LoginRequiredMixin,View):
    def get(self, request):
        form = ResetPasswordForm
        return render(request, 'users/reset_password.html', {'form':form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user = request.user
            user.set_password(new_password)
            user.save()
            return redirect('/')
        form = ResetPasswordForm
        return render(request, 'users/reset_password.html', {'form':form})
    


class EditTeacherView(AdminRequiredMixin, View):
    def get(self, request, id):
        teacher = Teacher.objects.filter(id=id).first()
        form = TeacherEditForm(instance=teacher)
        return render(request, 'users/edit_teacher.html', {'form': form})


    def post(self, request, id):
        teacher = get_object_or_404(Teacher, id=id)
        form = TeacherEditForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('users:students')
        return render(request, 'users/edit_teacher.html', {'form': form})
