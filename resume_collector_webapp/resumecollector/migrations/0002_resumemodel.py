# Generated by Django 3.2.12 on 2022-02-17 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumecollector', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=50)),
                ('cv', models.FileField(upload_to='User_CVs')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resume_uploader', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
