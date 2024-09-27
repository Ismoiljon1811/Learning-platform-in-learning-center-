# Generated by Django 5.0.4 on 2024-06-13 16:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('users', '0007_teacher_team_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='users.team'),
        ),
    ]