# Generated by Django 4.0.5 on 2022-06-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyApp', '0018_alter_post_image_alter_post_pracfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pracFile',
            field=models.FileField(blank=True, upload_to='files'),
        ),
    ]