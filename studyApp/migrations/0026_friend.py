# Generated by Django 4.0.5 on 2022-06-26 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studyApp', '0025_delete_peer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, default='', max_length=100)),
                ('lname', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='peers', to='studyApp.user')),
            ],
        ),
    ]