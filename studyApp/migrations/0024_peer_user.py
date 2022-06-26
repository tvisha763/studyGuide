# Generated by Django 4.0.5 on 2022-06-26 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studyApp', '0023_peer_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='peer',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='peers', to='studyApp.user'),
        ),
    ]
