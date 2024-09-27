from django.db import models
from users.models import Team, Student

class Lesson(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    homework_status = models.BooleanField(default=False)

    class Meta:
        unique_together = ['team', 'title']

    def __str__(self):
        return f"{self.title} {self.team}"


class Homework(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='homework')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    dascription = models.TextField()
    homework_file = models.FileField(upload_to='homeworks/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team',null = True, blank = True)

    class Meta:
        unique_together = ['lesson', 'student']


    def __str__(self):
        return f"{self.student.user.first_name} -- {self.lesson.title}"