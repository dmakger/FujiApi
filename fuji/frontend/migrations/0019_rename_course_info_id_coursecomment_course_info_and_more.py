# Generated by Django 4.0 on 2022-01-26 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_rename_date_create_coursecomment_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecomment',
            old_name='course_info_id',
            new_name='course_info',
        ),
        migrations.RenameField(
            model_name='coursefit',
            old_name='course_info_id',
            new_name='course_info',
        ),
        migrations.RenameField(
            model_name='courseinfo',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='courseskill',
            old_name='course_info_id',
            new_name='course_info',
        ),
        migrations.RenameField(
            model_name='coursestars',
            old_name='course_info_id',
            new_name='course_info',
        ),
    ]