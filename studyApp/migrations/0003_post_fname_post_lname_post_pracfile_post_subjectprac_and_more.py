# Generated by Django 4.0.5 on 2022-06-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyApp', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fname',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='lname',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='pracFile',
            field=models.FileField(blank=True, upload_to='practiceFiles'),
        ),
        migrations.AddField(
            model_name='post',
            name='subjectPrac',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='subjectsTutor',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='saleImgs'),
        ),
    ]
