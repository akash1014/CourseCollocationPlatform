# Generated by Django 2.2.10 on 2020-02-04 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('googleproject', '0002_user_info'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='course_info',
            new_name='course_track',
        ),
    ]