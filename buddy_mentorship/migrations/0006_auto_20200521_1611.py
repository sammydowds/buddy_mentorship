# Generated by Django 3.0.5 on 2020-05-21 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_mentorship', '0005_auto_20200511_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='want_help',
        ),
        migrations.AddField(
            model_name='experience',
            name='help_wanted',
            field=models.BooleanField(default=False),
        ),
    ]