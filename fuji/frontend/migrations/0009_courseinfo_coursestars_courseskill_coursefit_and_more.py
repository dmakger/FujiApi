# Generated by Django 4.0 on 2022-01-26 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('frontend', '0008_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_description', models.TextField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseStars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('five_stars_count', models.IntegerField()),
                ('four_stars_count', models.IntegerField()),
                ('three_stars_count', models.IntegerField()),
                ('two_stars_count', models.IntegerField()),
                ('one_stars_count', models.IntegerField()),
                ('course_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.courseinfo')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.courseinfo')),
            ],
        ),
        migrations.CreateModel(
            name='CourseFit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('course_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.courseinfo')),
            ],
        ),
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('stars_count', models.IntegerField()),
                ('course_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.courseinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]