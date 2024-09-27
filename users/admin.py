from django.contrib import admin
from .models import Student, Team, User, Teacher

admin.site.register(Student)

admin.site.register(Teacher)

admin.site.register(Team)

admin.site.register(User)

