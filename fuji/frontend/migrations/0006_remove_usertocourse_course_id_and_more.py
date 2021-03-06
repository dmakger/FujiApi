# Generated by Django 4.0 on 2022-01-09 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_course_lesson_module_profile_step_usertostep_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertocourse',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='usertocourse',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='usertolesson',
            name='lesson_id',
        ),
        migrations.RemoveField(
            model_name='usertolesson',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='usertomodule',
            name='module_id',
        ),
        migrations.RemoveField(
            model_name='usertomodule',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='usertostep',
            name='step_id',
        ),
        migrations.RemoveField(
            model_name='usertostep',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='UserToCourse',
        ),
        migrations.DeleteModel(
            name='UserToLesson',
        ),
        migrations.DeleteModel(
            name='UserToModule',
        ),
        migrations.DeleteModel(
            name='UserToStep',
        ),
    ]
