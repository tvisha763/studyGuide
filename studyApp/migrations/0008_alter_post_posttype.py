# Generated by Django 4.0.5 on 2022-06-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyApp', '0007_post_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postType',
            field=models.IntegerField(choices=[(1, 'Sale'), (2, 'Practice'), (3, 'Tutoring')], default=1),
        ),
    ]