# Generated by Django 4.0.5 on 2022-06-25 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='saleImgs')),
                ('description', models.CharField(blank=True, max_length=500)),
                ('postType', models.IntegerField(choices=[(1, 'None'), (2, 'Sale'), (3, 'Practice'), (4, 'Tutoring')], default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('sale', models.JSONField(blank=True, null=True)),
                ('practice', models.JSONField(blank=True, null=True)),
                ('tutor', models.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='studyApp.user')),
            ],
        ),
    ]