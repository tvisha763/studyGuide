# Generated by Django 4.0.5 on 2022-06-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyApp', '0003_post_fname_post_lname_post_pracfile_post_subjectprac_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='materialName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
